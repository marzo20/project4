from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vehicle(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    trim = models.CharField(max_length=50)
    bodystyle = models.CharField(max_length=50, default=None)
    year= models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Vehicle', default=None)
    vehicle_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.make

