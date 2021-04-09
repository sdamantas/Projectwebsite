from django.urls import path
from . import views


urlpatterns = [
    path('customer/<str:pk_test>/', views.customer),
]