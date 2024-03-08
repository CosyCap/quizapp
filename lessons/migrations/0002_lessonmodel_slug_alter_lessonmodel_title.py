# Generated by Django 5.0.2 on 2024-03-06 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lessons", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="lessonmodel",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name="lessonmodel",
            name="title",
            field=models.CharField(max_length=100),
        ),
    ]