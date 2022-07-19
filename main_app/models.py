from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField


# Create your models here.
class Vehicle(models.Model):
    vin = models.CharField(max_length=17, default=None)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    bodyClass = models.CharField(max_length=100)
    year= models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Vehicle', default=None)
    

    def __str__(self):
        return str(self.year) + " " + str(self.make) + " " + str(self.model)

class Post(models.Model):
    milage = models.IntegerField(max_length=10, default=None)
    content = models.TextField(default=None)
    vehicle_image = models.ImageField(null=True, blank=True, upload_to="images/")
    date = models.DateTimeField(auto_now=True)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return str(self.vehicle) + " : $" + str(self.price)

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='Post', default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Post', default=None)
    