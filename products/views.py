from django.shortcuts import render, redirect
from products.models import *
from products.forms import OrderForm

def product(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    out_for_delivery = orders.filter(status='Out for delivery').count()


    context = {'orders': orders, 'customers': customers,'total_customers':total_customers, 'total_orders':total_orders,'delivered': delivered,'pending':pending,'out_for_delivery':out_for_delivery}
    return render(request, 'dashboard.html', context)

def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request, 'order_form.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':

        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
    context = {'item':order}
    return render(request,'delete.html', context)