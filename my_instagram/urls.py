from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.home, name='my_instagram-home'),
    path('navbar/', views.navbar, name='my_instagram-navbar'),
]