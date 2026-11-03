from django.shortcuts import render, redirect
from .models import DetailsGPU, GPU
from django.http import HttpResponseRedirect, HttpResponseNotFound

# получение данных из бд
def index(request):
    gpu_details = DetailsGPU.objects.all().order_by('gpu_id')
    return render(request, "index.html", {"gpu_details": gpu_details})

def create(request):
    create_gpus()  # добавляем начальные данные для видеокарт

    # если запрос POST, сохраняем данные
    if request.method == "POST":
        gpu = GPU.objects.create(
            name=request.POST.get("name")
        )

        DetailsGPU.objects.create(
            memory_size=request.POST.get("memory_size"),
            frequency=request.POST.get("frequency"),
            gpu=gpu
        )

        return redirect('index')

    # передаем данные в шаблон
    details_gpu = DetailsGPU.objects.all()
    gpu = GPU.objects.all()
    return render(request, "create.html", {"details_gpu": details_gpu, "gpu":gpu})


def create_gpus():
    if DetailsGPU.objects.all().count() == 0:
        gpu1 = GPU.objects.create(name="Nvidia RTX 4090")
        #Account.user.objects.create(name="Иванов П.Л.")
        detail = DetailsGPU.objects.create(memory_size = 32, frequency= 8192, gpu = gpu1 )
        detail.gpu.save()


def edit(request, id):
    try:
        details_gpu = DetailsGPU.objects.get(gpu_id=id)
        if request.method == "POST":
            details_gpu.memory_size = request.POST.get("memory_size")
            details_gpu.frequency = request.POST.get("frequency")
            details_gpu.gpu.name = request.POST.get("name")

            details_gpu.gpu.save()
            details_gpu.save()

            return redirect('index')
        else:
            gpu = GPU.objects.get(id=details_gpu.gpu.id)
            return render(request, "edit.html", {"details_gpu": details_gpu, "gpu": gpu})
    except DetailsGPU.DoesNotExist:
        return HttpResponseNotFound("<h2>Details_GPU not found</h2>")

def delete(request, id):
    try:
        details_gpu = DetailsGPU.objects.get(gpu_id=id)
        details_gpu.delete()
        return redirect('index')
    except DetailsGPU.DoesNotExist:
        return HttpResponseNotFound("<h2>GPU not found</h2>")