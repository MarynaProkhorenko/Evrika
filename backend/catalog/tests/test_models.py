from django.test import TestCase
from catalog.models import Course, Order


class CourseModelTests(TestCase):
    """Should check representation method in Course model"""
    def setUp(self):
        self.course = Course.objects.create(
            title="Mathematics",
            teacher="John Smith",
            description="A course on algebra and calculus",
            duration=60,
            age_of_pupils=15,
            price=50.00,
            school_subject=True,
            image=None,
        )

    def test_course_str(self):
        self.assertEqual(
            str(self.course),
            (f"{self.course.title}( {self.course.age_of_pupils}"
             f" years, {self.course.duration} month)")
        )


class OrderModelTests(TestCase):
    """Should check __str__ method & order.total_price in Order models"""
    def setUp(self):
        self.order = Order.objects.create(
            user_id=1, total_cost=0.0,
        )
        self.course_1 = Course.objects.create(
            title="Mathematics",
            teacher="John Smith",
            description="A course on algebra and calculus",
            duration=60,
            age_of_pupils=15,
            price=50.00,
            school_subject=True,
            image=None,
        )
        self.course_2 = Course.objects.create(
            title="Physics",
            teacher="Jane Doe",
            description="A course on classical mechanics and thermodynamics",
            duration=8,
            age_of_pupils=17,
            price=60.00,
            school_subject=True,
            image=None,
        )
        self.order.courses.add(self.course_1)
        self.order.courses.add(self.course_2)

    def test_order_str(self):
        self.assertEqual(
            str(self.order), str(self.order.created_at)
        )

    def test_total_price(self):
        self.assertEqual(self.order.total_price, 110.00)
