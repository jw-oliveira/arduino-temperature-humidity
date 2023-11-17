from django.db import models

# Create your models here.


class Records(models.Model):
    temperature = models.CharField(max_length=10)
    humidity = models.CharField(max_length=10)
    registry_date = models.DateTimeField()
