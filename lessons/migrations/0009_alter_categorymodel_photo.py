# Generated by Django 5.0.2 on 2024-03-06 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lessons", "0008_categorymodel_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categorymodel",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="products/"),
        ),
    ]