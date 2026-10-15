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

def redirect_to_navigator(_):
    return HttpResponseRedirect("/navigator")