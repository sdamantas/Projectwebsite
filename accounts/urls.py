from django.urls import path
from django.http import HttpResponse
from accounts import views

urlpatterns = [
    path('customer/', views.customer),


]