from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect

from Z3app.models import Client, GPU, Spec


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
    create_gpus_new()
    gpus = GPU.objects.all()
    return render(request, "products.html", {"gpus": gpus})

def create_gpus_new():
    if GPU.objects.all().count() == 0:
        spec1 = Spec.objects.create(frequency=2280, memory_type="GDDR7", memory_size=8)
        GPU.objects.create(name="Nvidia RTX 5060", price=50000, spec=spec1)

        spec2 = Spec.objects.create(frequency=2407, memory_type="GDDR7", memory_size=16)
        GPU.objects.create(name="Nvidia RTX 5060 Ti", price=80000, spec=spec2)

        spec3 = Spec.objects.create(frequency=2325, memory_type="GDDR7", memory_size=12)
        GPU.objects.create(name="Nvidia RTX 5070", price=90000, spec=spec3)

        spec4 = Spec.objects.create(frequency=2295, memory_type="GDDR7", memory_size=16)
        GPU.objects.create(name="Nvidia RTX 5070 Ti", price=150000, spec=spec4)

        spec5 = Spec.objects.create(frequency=1875, memory_type="GDDR7", memory_size=16)
        GPU.objects.create(name="Nvidia RTX 5080", price=240000, spec=spec5)

        spec6 = Spec.objects.create(frequency=2017, memory_type="GDDR7", memory_size=32)
        GPU.objects.create(name="Nvidia RTX 5090", price=800000, spec=spec6)

def sale(request):
    return render(request, "sale.html")

def sale_progress(request):
    return render(request, "sale_progress.html")

