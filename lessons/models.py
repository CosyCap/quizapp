from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Category(models.Model):
    lesson_name = models.CharField(max_length=255, verbose_name='Название урока')
    slug = models.SlugField(verbose_name='URL', unique=True)
    min_description = models.TextField(max_length=100, verbose_name='Краткое описание урока')
    image = models.ImageField(upload_to='description_lesson/', blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return self.lesson_name

from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField 
class Lesson(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Титул урока')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    image = models.ImageField(upload_to='lesson_image/', blank=True, null=True, verbose_name='Изображение урока')
    lesson = RichTextField(verbose_name='Текст урока')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='lessons', null=True)
    link = models.TextField(blank=True, null=True, verbose_name='Ссылка')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title 

