from django.db import models

# Create your models here.
class location(models.Model):
    city= models.CharField(max_length=20)
    latitude=models.FloatField()
    longitude=models.FloatField()

class tempEntry(models.Model):
    temp=models.IntegerField()
    time=models.IntegerField()
    place=models.ForeignKey(location, on_delete=models.CASCADE, default=1)

