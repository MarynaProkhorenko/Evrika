# Generated by Django 4.1.7 on 2023-03-31 13:25

import catalog.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0005_order_total_coast_alter_course_age_of_pupils"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="image",
            field=models.ImageField(
                null=True, upload_to=catalog.models.movie_image_file_path
            ),
        ),
    ]