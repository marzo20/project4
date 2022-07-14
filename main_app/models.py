from django.db import models

# Create your models here.
class Vehicle(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    trim = models.CharField(max_length=50)
    year= models.IntegerField()

    def __str__(self):
        return self.make

