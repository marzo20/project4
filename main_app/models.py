from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vehicle(models.Model):
    vin = models.CharField(max_length=17, default=None)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    bodyClass = models.CharField(max_length=100)
    year= models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Vehicle', default=None)
    # vehicle_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.vin

