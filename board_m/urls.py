
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('board/create/', views.create_board, name='creat')
]
