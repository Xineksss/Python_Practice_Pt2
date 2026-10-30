from django.db import models


class GPU(models.Model):
    brand = models.CharField(max_length=25)  # Поле из символов
    model = models.CharField(max_length=25)  # Поле из символов
    video_memory_size = models.IntegerField()
    video_memory_type = models.CharField(max_length=25)

    objects = models.Manager()
    DoesNotExist = models.Manager
