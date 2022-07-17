from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vin','make', 'model', 'bodyClass', 'year', 'vehicle_image']

