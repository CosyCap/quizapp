from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path('', views.main, name = "index"),
]