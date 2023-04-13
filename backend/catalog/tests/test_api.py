from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from catalog.models import Course
from user.models import User


class CourseViewSetTestCase(APITestCase):
    def setUp(self):
        self.course1 = Course.objects.create(
            title="Course 1",
            description="Description for course 1",
            duration=10,
            age_of_pupils=8,
            school_subject=True,
        )
        self.course2 = Course.objects.create(
            title="Course 2",
            description="Description for course 2",
            duration=20,
            age_of_pupils=10,
            school_subject=True,
        )

    def test_list_courses(self):
        url = reverse("catalog:course-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_courses_by_title(self):
        url = reverse("catalog:course-list")
        response = self.client.get(url, {"title": "Course 1,Course 2"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_courses_by_duration(self):
        url = reverse("catalog:course-list")
        response = self.client.get(url, {"duration": "10,20"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_courses_by_age_of_pupils(self):
        url = reverse("catalog:course-list")
        response = self.client.get(url, {"age_of_pupils": "8,10"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_courses_by_school_subject(self):
        url = reverse("catalog:course-list")
        response = self.client.get(url, {"school_subject": "true"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class OrderViewSetTestCase(APITestCase):
    def setUp(self):
        self.course1 = Course.objects.create(
            title="Course 1",
            description="Description for course 1",
            duration=10,
            age_of_pupils=8,
            school_subject=True,
        )
        self.course2 = Course.objects.create(
            title="Course 2",
            description="Description for course 2",
            duration=20,
            age_of_pupils=10,
            school_subject=True,
        )
        self.user = User.objects.create_user(
            email="testuser@example.com",
            password="testpass",
        )

    def test_create_order(self):
        url = reverse("catalog:order-list")
        data = {"courses": [self.course1.id, self.course2.id]}
        self.client.force_authenticate(self.user)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
