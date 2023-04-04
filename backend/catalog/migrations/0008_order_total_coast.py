# Generated by Django 4.1.7 on 2023-04-04 07:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0007_remove_order_total_coast_alter_course_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="total_coast",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]