from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=30)

class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.IntegerField()

    objects=models.Manager()
    DoesNotExist=models.Manager

