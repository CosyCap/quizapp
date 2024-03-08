from django.urls import path
from . import views

app_name = 'lessons'

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('<slug:lesson_slug>/', views.lesson, name='lesson')
]
