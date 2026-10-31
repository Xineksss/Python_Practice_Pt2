from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import Model, Brand

def index(request):
    models = Model.objects.all()
    return render(request, "index.html", {"models": models})


def create(request):
    create_brands()  # добавляем начальные данные для компаний
    # если   запрос POST, сохраняем данные
    if request.method == "POST":
        model = Model()
        model.name = request.POST.get("name")
        model.price = request.POST.get("price")
        model.brand_id = request.POST.get("brand_id")
        model.save()
        return redirect("index")
    # передаем данные в шаблон
    brands = Brand.objects.all()
    return render(request, "create.html", {"brands": brands})

def create_brands():
    if Brand.objects.all().count() == 0:
        Brand.objects.create(name="AMD")
        Brand.objects.create(name="Nvidia")
        Brand.objects.create(name="Intel")


# изменение данных в бд
def edit(request, id):
    try:
        model = Model.objects.get(id=id)

        if request.method == "POST":
            model.name = request.POST.get("name")
            model.price = request.POST.get("price")
            model.brand_id = request.POST.get("brand")
            model.save()
            return redirect("index")
        else:
            brands = Brand.objects.all()
            return render(request, "edit.html", {"model": model, "brands": brands})
    except Model.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")

def delete(request, id):
    try:
        model = Model.objects.get(id=id)
        model.delete()
        return HttpResponseRedirect("/")
    except Model.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")



