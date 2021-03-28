from django.shortcuts import render

def product(request):
    return render(request, 'product.html')
def home(request):
    return render(request, 'dashboard.html')