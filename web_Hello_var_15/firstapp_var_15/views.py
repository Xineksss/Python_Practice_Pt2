import os
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
import pandas as pd
from . import forms

def navigator(request):
    return render(request, "navigator.html")

def graphic_cards(request):
    df = pd.read_excel(os.path.join(settings.BASE_DIR, "firstapp_var_15", "tablica", "gpu.xlsx"))
    headers = df.columns.tolist()
    data = df.to_dict("records")
    context = {
        "headers": headers,
        "data": data,
        "title": "Видеокарты"
    }
    return render(request, "graphic_cards.html", context)

def processors(request):
    df = pd.read_excel(os.path.join(settings.BASE_DIR, "firstapp_var_15", "tablica", "case.xlsx"))
    headers = df.columns.tolist()
    data = df.to_dict("records")
    context = {
        "headers": headers,
        "data": data,
        "title": "Процессоры"
    }
    return render(request, "processors.html", context)

def motherboards(request):
    df = pd.read_excel(os.path.join(settings.BASE_DIR, "firstapp_var_15", "tablica", "case.xlsx"))
    headers = df.columns.tolist()
    data = df.to_dict("records")
    context = {
        "headers": headers,
        "data": data,
        "title": "Материнские платы"
    }
    return render(request, "motherboards.html", context)

def ram(request):
    df = pd.read_excel(os.path.join(settings.BASE_DIR, "firstapp_var_15", "tablica", "case.xlsx"))
    headers = df.columns.tolist()
    data = df.to_dict("records")
    context = {
        "headers": headers,
        "data": data,
        "title": "Оперативная память"
    }
    return render(request, "ram.html", context)

def power_supply(request):
    df = pd.read_excel(os.path.join(settings.BASE_DIR, "firstapp_var_15", "tablica", "case.xlsx"))
    headers = df.columns.tolist()
    data = df.to_dict("records")
    context = {
        "headers": headers,
        "data": data,
        "title": "Блоки питания"
    }
    return render(request, "power_supply.html", context)

def cases(request):
    df = pd.read_excel(os.path.join(settings.BASE_DIR, "firstapp_var_15", "tablica", "case.xlsx") )
    headers = df.columns.tolist()
    data = df.to_dict("records")
    context = {
        "headers": headers,
        "data": data,
        "title": "Корпуса"
    }
    return render(request, "cases.html", context)

def ssd(request):
    df = pd.read_excel(os.path.join(settings.BASE_DIR, "firstapp_var_15", "tablica", "ssd.xlsx"))
    headers = df.columns.tolist()
    data = df.to_dict("records")
    context = {
        "headers": headers,
        "data": data,
        "title": "SSD"
    }
    return render(request, "ssd.html", context)

def hdd(request):
    df = pd.read_excel(os.path.join(settings.BASE_DIR, "firstapp_var_15", "tablica", "hdd.xlsx"))
    headers = df.columns.tolist()
    data = df.to_dict("records")
    context = {
        "headers": headers,
        "data": data,
        "title": "HDD"
    }
    return render(request, "hdd.html", context)

def redirect_to_home(_):
    return HttpResponseRedirect("/home")

def home(request):
    return render(request, 'home.html')

def home(request):
    content_list = gettabl()
    return render(request, 'home.html', context={'content_list': content_list})

def gettabl():
    cat = []
    dirpath = os.path.dirname(os.path.abspath(__file__))

    f = open(dirpath + "/tablica/about_us.txt", "r", encoding="utf-8")

    for line in f:
        cat.append(line)

    f.close()
    return cat

def client(request):
    userform = forms.UserForm
    return render(request, "client.html",{"form":userform})

def postuser(request):
    name = request.POST.get("name", "Undefined") # по умолчанию
    surname = request.POST.get("surname", "Undefined")   # по умолчанию
    return HttpResponse(f"<h2>Имя: {name} Фамилия: {surname}</h2>")



