# Generated by Django 5.0.2 on 2024-03-07 08:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lessons", "0019_lesson_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="lesson",
            field=ckeditor.fields.RichTextField(verbose_name="Текст урока"),
        ),
    ]
