from django.db import models

class GPU(models.Model):
    name = models.CharField(max_length=30)
    objects=models.Manager()
    DoesNotExit=models.Manager


class Customer(models.Model):
    name = models.CharField(max_length=30)
    courses = models.ManyToManyField(GPU, through="Enrollment")


class Enrollment(models.Model):
    student = models.ForeignKey(Customer, on_delete=models.CASCADE)
    gpu = models.ForeignKey(GPU, on_delete=models.CASCADE)
    date = models.DateField()  # дата покупки
    price = models.IntegerField()  # цена

