from django.urls import path, include
from rest_framework import routers

from catalog.views import CourseViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register("courses", CourseViewSet)
router.register("orders", OrderViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "catalog"
