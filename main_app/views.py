from xmlrpc.client import ResponseError
from django.contrib import messages
from django.shortcuts import redirect, render
import requests
from .form import VehicleForm
from .registerform import NewUserForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Vehicle
from django.contrib.auth.forms import AuthenticationForm
import json
# Create your views here.


#Define the home view
def home(request):
    return render(request, "home.html")

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login_form.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")

def vehicles(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicle_list.html', {'vehicles':vehicles})

def index(request):
    url = "https://vin-decoder19.p.rapidapi.com/vin_decoder_lite"
    querystring = request.GET.get('VIN')

    headers = {
	"X-RapidAPI-Key": "3c7019782cmsh543dfafbdcda7cbp11c5a2jsn177cb39c544a",
	"X-RapidAPI-Host": "vin-decoder19.p.rapidapi.com"
}

    response = requests.get(url, headers=headers, params={"vin":querystring})
    info = response.json()
    context = {
        'info' : info
    } 
    if (
    response.status_code != 204 and
    response.headers["content-type"].strip().startswith("application/json")
):
        try:
            return render(request,'info.html', context)
        except ValueError:
        # decide how to ha
            return render('home.html')
     

@login_required(login_url='/login/')
def vehicle_create(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            vehicle = form.save()
            return redirect('vehicles')
    else:
        form = VehicleForm()
    context = {'form': form, 'header': 'Add vehicle information'}
    return render(request, 'vehicle_form.html', context)

def vehicle_edit(request, pk):
    vehicle = Vehicle.objects.get(pk=pk)
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            vehicle = form.save()
            return redirect('vehicles')
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'vehicle_form.html',{'form': form})

def vehicle_delete(request, pk):
    Vehicle.objects.get(pk=pk).delete()
    return redirect('vehicles')

def profile_show(request):
    if request.user.is_authenticated:
    # Do something for authenticated users.
        return render(request, 'profile.html')
    else:
        return HttpResponse('<h1>Something went wrong with login</h1>')