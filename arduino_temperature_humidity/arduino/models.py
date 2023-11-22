from django.db import models

class Records(models.Model):
    temperature = models.CharField(max_length=5)
    humidity = models.CharField(max_length=5)
    registry_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = "arduino_records"
