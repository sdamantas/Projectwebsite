from django.urls import path
from django.http import HttpResponse
from products import views

urlpatterns = [
    path('', views.home),
    path('products/', views.product),
    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>', views.deleteOrder, name="delete_order"),


]