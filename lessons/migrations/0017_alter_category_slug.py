# Generated by Django 5.0.2 on 2024-03-07 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lessons", "0016_alter_lesson_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(unique=True, verbose_name="URL"),
        ),
    ]
