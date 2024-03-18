from django.urls import path, include
from booksinfo import views


urlpatterns = [
    path('', views.index, name='index'),
]