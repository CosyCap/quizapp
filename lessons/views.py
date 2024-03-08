from django.shortcuts import render, get_object_or_404
from .models import Category, Lesson

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'lessons/category_list.html', {'categories': categories})

def lesson(request, lesson_slug):
    lesson = get_object_or_404(Lesson, slug=lesson_slug)
    return render(request, 'lessons/category_detail.html', {'lesson': lesson})

