from django.db import models


class GPU(models.Model):
    name=models.CharField(max_length=20)
    objects = models.Manager()
    DoesNotExist = models.Manager


class DetailsGPU(models.Model):
    memory_size=models.IntegerField()
    frequency=models.IntegerField()
    gpu=models.OneToOneField(GPU,on_delete=models.CASCADE,primary_key=True)
    objects = models.Manager()
    DoesNotExist = models.Manager
