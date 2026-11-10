from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect

from Z3app.models import Client


# Create your views here.

def index(request):
    return render(request, "index.html")


def customers(request):
    clients = Client.objects.all()
    return render(request, "customers.html", {"clients": clients})


def create_client(request):
    if request.method == "POST":
        client = Client()
        client.name = request.POST.get("client")
        client.save()
        return redirect('customers')
    return redirect('customers')


def delete_client(request, id):
    try:
        person = Client.objects.get(id=id)
        person.delete()
        return redirect('customers') # Возвращаемся к списку
    except Client.DoesNotExist:
        return HttpResponseNotFound("<h2> Клиент не найден </h2>")

def products(request):
    return render(request, "products.html")

def sale(request):
    return render(request, "sale.html")

def sale_progress(request):
    return render(request, "sale_progress.html")

