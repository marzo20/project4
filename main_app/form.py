from django import forms
from .models import Vehicle
from. models import Post

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vin','make', 'model', 'bodyClass', 'year']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['vehicle', 'vehicle_image', 'price']
    
    def __init__(self, user, *args, **kwargs):
        # user = kwargs.pop('user', None)
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['vehicle'].queryset = Vehicle.objects.filter(user_id=user)