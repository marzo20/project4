from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vehicle(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    trim = models.CharField(max_length=50)
    year= models.IntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Vehicles', default=None)

    def __str__(self):
        return self.make

