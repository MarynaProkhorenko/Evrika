from rest_framework import serializers

from catalog.models import Course, Order


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "teacher",
            "description",
            "duration",
            "age_of_pupils",
            "price",
            "school_subject",
            "image_url",
            "image",
        )


class CourseListSerializer(CourseSerializer):
    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "duration",
            "age_of_pupils",
            "school_subject",
            "price",
            "image",
            "image_url",
        )


class CourseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "image")


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ("id", "created_at", "courses", "total_price")
