from django.urls import path
from . import views

app_name = 'tests'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('get_quiz/', views.get_quiz, name = 'get_quiz'),
    path('quiz/', views.quiz, name = 'quiz'),
]
