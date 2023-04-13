from django.test import TestCase
from catalog.models import Course
from catalog.serializers import (
    CourseSerializer,
    CourseListSerializer,
    CourseImageSerializer,
)


class CourseSerializerTestCase(TestCase):
    """Should test expected fields in Course serializer"""
    def setUp(self):
        self.course = Course.objects.create(
            title="Mathematics",
            teacher="John Doe",
            description="An introductory course in mathematics",
            duration=4,
            age_of_pupils="12",
            price=50,
            school_subject=True
        )
        self.serializer = CourseSerializer(instance=self.course)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), [
            "id",
            "title",
            "teacher",
            "description",
            "duration",
            "age_of_pupils",
            "price",
            "school_subject"
        ])

    def test_title_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["title"], "Mathematics")


class CourseListSerializerTestCase(TestCase):
    """Should expected fields in course list serializer"""
    def setUp(self):
        self.course = Course.objects.create(
            title="Mathematics",
            teacher="John Doe",
            description="An introductory course in mathematics",
            duration=4,
            age_of_pupils="12",
            price=50,
            school_subject=True
        )
        self.serializer = CourseListSerializer(instance=self.course)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), [
            "id", "title", "duration", "age_of_pupils", "price"
        ])

    def test_title_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["title"], "Mathematics")


class CourseImageSerializerTestCase(TestCase):
    """Should check save img to /media/image.jpg"""
    def setUp(self):
        self.course = Course.objects.create(
            title="Mathematics",
            teacher="John Doe",
            description="An introductory course in mathematics",
            duration=4,
            age_of_pupils="12",
            price=50,
            school_subject=True,
            image="image.jpg"
        )
        self.serializer = CourseImageSerializer(instance=self.course)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ["id", "image"])

    def test_image_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["image"], "/media/image.jpg")
