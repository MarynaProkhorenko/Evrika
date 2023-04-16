from typing import Type, List

from django.db.models import QuerySet
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.viewsets import GenericViewSet

from catalog.email_notification import send_email
from catalog.models import Course, Order
from catalog.serializers import CourseSerializer, CourseListSerializer, OrderSerializer

from catalog.serializers import CourseImageSerializer


class CoursePagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100


class CourseViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    pagination_class = CoursePagination

    @staticmethod
    def _params_to_list(qs) -> List[str]:
        return [param for param in qs.split(",")]

    @staticmethod
    def _params_to_ints(qs) -> List[int]:
        return [int(str_num) for str_num in qs.split(",")]

    def get_queryset(self) -> QuerySet:
        title = self.request.query_params.get("title")
        duration = self.request.query_params.get("duration")
        age_of_pupils = self.request.query_params.get("age_of_pupils")
        school_subject = self.request.query_params.get("school_subject")

        queryset = self.queryset

        if title:
            titles = self._params_to_list(title)
            queryset = queryset.filter(title__in=titles)

        if duration:
            durations = self._params_to_ints(duration)
            queryset = queryset.filter(duration__in=durations)

        if age_of_pupils:
            ages = self._params_to_ints(age_of_pupils)
            queryset = queryset.filter(age_of_pupils__in=ages)

        if school_subject:
            queryset = queryset.filter(school_subject=bool(school_subject))

        return queryset.distinct()

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="title",
                type={"type": "list", "items": {"type": "str"}},
                description="Filter by title",
                required=False,
            ),
            OpenApiParameter(
                name="duration",
                type={"type": "list", "items": {"type": "number"}},
                description="Filter by duration",
                required=False,
            ),
            OpenApiParameter(
                name="age_of_pupils",
                type={"type": "list", "items": {"type": "number"}},
                description="Filter by age_of_pupils",
                required=False,
            ),
            OpenApiParameter(
                name="school_subject",
                type=OpenApiTypes.BOOL,
                description="Filter by school_subject",
                required=False,
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_serializer_class(self) -> Type[Serializer]:
        if self.action == "list":
            return CourseListSerializer

        if self.action == "upload_image":
            return CourseImageSerializer

        return CourseSerializer

    @action(
        methods=["POST"],
        detail=True,
        url_path="upload-image",
        permission_classes=[IsAdminUser]
    )
    def upload_image(self, request, pk=None) -> Response:
        course = self.get_object()
        serializer = self.get_serializer(course, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderViewSet(
    mixins.CreateModelMixin,
    GenericViewSet,
):
    queryset = Order.objects.prefetch_related(
        "courses"
    )
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self) -> QuerySet:
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer) -> None:
        order = serializer.save(user=self.request.user)
        order.total_cost = order.total_price
        order.save()

        courses = ',\n '.join([str(course) for course in order.courses.all()])
        full_name = order.user.first_name + " " + order.user.last_name
        total_cost = order.total_cost
        receiver_email = order.user.email

        send_email(courses, full_name, total_cost, receiver_email)
