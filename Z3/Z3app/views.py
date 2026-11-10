from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect

from Z3app.models import Client, GPU, Spec, Purchase


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

def edit_client(request, id):
    client = Client.objects.get(id=id)
    if request.method == "POST":
        client.name = request.POST.get("client")
        client.save()
        return redirect('customers')
    return render(request, "edit_client.html", {"client": client})

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

def purchase(request):
    if request.method == "POST":
        sale = Purchase()
        sale.date_order = request.POST.get("date")
        sale.amount = request.POST.get("amount")
        sale.client_id = request.POST.get("client")
        sale.gpu_id = request.POST.get("gpu")
        sale.save()
        return render(request, "success_buy.html", {"sale": sale})

    sales= Purchase.objects.all()
    gpus= GPU.objects.all()
    clients=Client.objects.all()
    return render(request, "sale.html", {"sales": sales,"gpus":gpus,"clients":clients})

def sale_progress(request):
    sales = Purchase.objects.all()
    return render(request,"sale_progress.html",{"sales":sales})

