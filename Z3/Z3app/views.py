from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def customers(request):
    return render(request, "customers.html")

def products(request):
    return render(request, "products.html")

def sale(request):
    return render(request, "sale.html")

def sale_progress(request):
    return render(request, "sale_progress.html")