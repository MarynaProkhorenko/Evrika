from typing import Type

from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import Serializer
from rest_framework.viewsets import GenericViewSet

from catalog.models import Course, Order
from catalog.serializers import CourseSerializer, CourseListSerializer, OrderSerializer


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
    def _params_to_list(qs):
        return [param for param in qs.split(",")]

    @staticmethod
    def _params_to_ints(qs):
        return [int(str_num) for str_num in qs.split(",")]

    def get_queryset(self):
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

        return queryset

    def get_serializer_class(self) -> Type[Serializer]:
        if self.action == "list":
            return CourseListSerializer

        return CourseSerializer


class OrderViewSet(
    mixins.CreateModelMixin,
    GenericViewSet,
):
    queryset = Order.objects.prefetch_related(
        "courses"
    )
    serializer_class = OrderSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
