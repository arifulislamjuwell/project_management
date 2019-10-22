
from django.urls import path,include
from . import views
urlpatterns = [
    path('login/', views.login, name='login'),
    path('singup/', views.singup, name='singup')
]
