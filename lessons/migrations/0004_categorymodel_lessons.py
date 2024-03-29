# Generated by Django 5.0.2 on 2024-03-06 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lessons", "0003_categorymodel"),
    ]

    operations = [
        migrations.AddField(
            model_name="categorymodel",
            name="lessons",
            field=models.ManyToManyField(
                related_name="categories", to="lessons.lessonmodel"
            ),
        ),
    ]
