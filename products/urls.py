from django.urls import path
from django.http import HttpResponse
from products import views

urlpatterns = [
    path('', views.home),
    path('products/', views.product),


]