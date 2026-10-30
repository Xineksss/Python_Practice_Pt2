from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template.response import HttpResponse,TemplateResponse
from .models import GPU

def index(request):
    gpus = GPU.objects.all()
    return render(request,"gpu.html",{"gpus":gpus})


def create(request):
    if request.method=="POST":
        gpus= GPU()
        gpus.brand=request.POST.get("brand")
        gpus.model=request.POST.get("model")
        gpus.video_memory_size=request.POST.get("video_memory_size")
        gpus.video_memory_type=request.POST.get("video_memory_type")
        gpus.save()
    return redirect('index')


def edit(request,id):
    try:
        gpus=GPU.objects.get(id=id)
        if request.method=="POST":
            gpus.brand = request.POST.get("brand")
            gpus.model = request.POST.get("model")
            gpus.video_memory_size = request.POST.get("video_memory_size")
            gpus.video_memory_type = request.POST.get("video_memory_type")
            gpus.save()
            return redirect('index')
        else:
            return render(request,"edit.html",{"gpus":gpus})
    except GPU.DoesNotExist:
        return HttpResponseNotFound("<h2> Клиент не найден</h2>")

def delete(request,id):
    try:
        gpus=GPU.objects.get(id=id)
        gpus.delete()
        return HttpResponseRedirect("/")
    except GPU.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")
