# Generated by Django 4.1.7 on 2023-03-31 08:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0003_alter_course_duration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="duration",
            field=models.IntegerField(),
        ),
    ]