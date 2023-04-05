import os
import uuid

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from django.conf import settings
from django.utils.text import slugify


def movie_image_file_path(instance, filename) -> str:
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.title)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/images/", filename)


class Course(models.Model):
    title = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    age_of_pupils = models.IntegerField(
        validators=[MinValueValidator(7), MaxValueValidator(18)]
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0
    )
    school_subject = models.BooleanField()
    image = models.ImageField(null=True, upload_to=movie_image_file_path)

    def __str__(self) -> str:
        return f"{self.title}( {self.age_of_pupils} years, {self.duration} month)"


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    courses = models.ManyToManyField(Course)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    total_cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0
    )

    def __str__(self) -> str:
        return str(self.created_at)

    class Meta:
        ordering = ["-created_at"]

    @property
    def total_price(self):
        total = 0
        for course in self.courses.all():
            total += course.price
        return total
