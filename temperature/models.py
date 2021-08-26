from django.db import models

# Create your models here.
class location(models.Model):
    city= models.CharField(max_length=20)
    latitude=models.FloatField()
    longitude=models.FloatField()
    access_key=models.CharField(max_length=200)

class tempEntry(models.Model):
    temp=models.FloatField()
    time=models.IntegerField()
    place=models.ForeignKey(location, on_delete=models.CASCADE, default=1)

