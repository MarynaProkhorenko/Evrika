from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from django.conf import settings


class Course(models.Model):
    title = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    age_of_pupils = models.IntegerField(
        validators=[MinValueValidator(7), MaxValueValidator(18)]
    )
    price = models.IntegerField()
    school_subject = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.title}( {self.age_of_pupils} years, {self.duration} month)"


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    courses = models.ManyToManyField(Course)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    total_coast = models.IntegerField()

    def __str__(self) -> str:
        return str(self.created_at)

    class Meta:
        ordering = ["-created_at"]
