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
            "school_subject"
        )


class CourseListSerializer(CourseSerializer):
    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "duration",
            "age_of_pupils",
            "price",
        )


class CourseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "image")


class OrderSerializer(serializers.ModelSerializer):
   # courses = CourseSerializer(many=True, read_only=True, allow_empty=False)

    class Meta:
        model = Order
        fields = ("id", "created_at", "courses", "total_price")
