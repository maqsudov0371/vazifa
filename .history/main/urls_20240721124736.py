from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.products, name='PRODUCTS'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('products/', views.products, name='products'),
]