# Generated by Django 5.0.2 on 2024-03-07 07:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lessons", "0015_lesson_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lessons",
                to="lessons.category",
            ),
        ),
    ]
