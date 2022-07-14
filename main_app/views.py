from xmlrpc.client import ResponseError
from django.shortcuts import redirect, render
from .form import VehicleForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Vehicle
# Create your views here.


#Define the home view
def home(request):
    return HttpResponse('<h1>Niche Market<h1>')

def vehicles(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicle_list.html', {'vehicles':vehicles})

def vehicle_create(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save()
            return redirect('vehicles')
    else:
        form = VehicleForm()
    context = {'form': form, 'header': 'Add vehicle information'}
    return render(request, 'vehicle_form.html', context)

def vehicle_edit(request, pk):
    vehicle = Vehicle.objects.get(pk=pk)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            vehicle = form.save()
            return redirect('vehicles')
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'vehicle_form.html',{'form': form})

def login_page(request):
    return render(request, 'login_form.html')

def profile_show(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request,user)
        return render(request, 'profile.html')
    else:
        return HttpResponse('<h1>Something went wrong with login</h1>')

def logout_view(request):
    logout(request)
    return redirect('login_page')