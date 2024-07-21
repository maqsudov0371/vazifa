from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blogs, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('product')
]