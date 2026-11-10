from django.db import models


class Spec(models.Model):
    frequency = models.IntegerField()
    memory_type = models.CharField(max_length=20)
    memory_size = models.IntegerField()


class GPU(models.Model):
    name=models.CharField(max_length=20)
    price=models.FloatField()
    spec = models.OneToOneField(Spec, on_delete=models.CASCADE, primary_key=True)
    objects=models.Manager()
    DoesNotExist=models.Manager

class Client(models.Model):
    name=models.CharField(max_length=20)
    objects = models.Manager()
    DoesNotExist = models.Manager

class Purchase(models.Model):
    date_order = models.DateField()
    amount = models.IntegerField()
    gpu = models.ForeignKey(GPU,on_delete=models.CASCADE)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    objects = models.Manager()
    DoesNotExist = models.Manager
