import os
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def navigator(request):
    return render(request, "navigator.html")

def graphic_cards(request):
    return render(request, "graphic_cards.html")

def processors(request):
    return render(request, "processors.html")

def motherboards(request):
    return render(request, "motherboards.html")

def ram(request):
    return render(request, "ram.html")

def power_supply(request):
    return render(request, "power_supply.html")

def cases(request):
    return render(request, "cases.html")

def ssd(request):
    return render(request, "ssd.html")

def hdd(request):
    return render(request, "hdd.html")

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