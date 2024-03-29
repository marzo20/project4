from urllib import response
from xmlrpc.client import ResponseError
from django.contrib import messages
from django.shortcuts import redirect, render
import requests
from .form import VehicleForm
from .form import PostForm
from .registerform import NewUserForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Vehicle
from .models import Post
from django.contrib.auth.forms import AuthenticationForm
import json
# Create your views here.


#Define the home view
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

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

def posts(request):
    posts = Post.objects.all()
    return render(request, 'vehicle_list.html', {'posts':posts})

@login_required(login_url='/login/')
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    # vehicle = Vehicle.objects.get(pk=post.vehicle)
    context = {
        'post': post,
        # 'vehicle': vehicle
    }
    return render(request, 'post_detail.html', context)

@login_required(login_url='/login/')
def info(request):
    return render(request, 'info.html')

def index(request):
    querystring = request.GET.get('VIN')
    print(querystring, 'querystring test')
    url = f"https://cis-vin-decoder.p.rapidapi.com/vinDecode"
    # querystring = request.GET.get('VIN')
    headers = {
	"X-RapidAPI-Key": "3c7019782cmsh543dfafbdcda7cbp11c5a2jsn177cb39c544a",
	"X-RapidAPI-Host": "cis-vin-decoder.p.rapidapi.com"
}
    
    response = requests.request("GET", url, headers=headers, params={"vin":querystring})
    info = response.text
    info_json = json.loads(info)
    # data = {
    #     "brandName": response["brandName"],
    #     "modelName": response["modelName"],
    # }
    print(url)
    print(info_json)
    return render(request,'details.html', {'data':info_json,
    'vin': querystring})

@login_required(login_url='/login/')
def post_create(request):
    if request.method == 'POST':
        print('this is post' , request.POST)
        print('this is user' , request.user)
        form = PostForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            print(request.user)
            # vehicle = Vehicle.objects.filter(vin= PostForm('vehicle'))
            # vehicle_id = vehicle.id
            # form.instance.vehicle = vehicle_id
            post = form.save()
            print(post)
            return redirect('posts')
    else:
        form = PostForm(user=request.user)
    context = {'form': form, 'header': 'Add vehicle information'}
    return render(request, 'post_form.html', context)


@login_required(login_url='/login/')
def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    if post.user != request.user:
        return redirect('no_access')
    if request.method == 'POST':
        form = PostForm(request.user, request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('posts')
    else:
        form = PostForm(instance=post, user=request.user)
        return render(request, 'post_form.html',{'form': form})
    

@login_required(login_url='/login/')
def post_delete(request, pk):
    if request.user.is_authenticated:
        post=Post.objects.get(pk=pk)
        if post.user == request.user:
            post.delete()
            return redirect('posts')
        else:
            return redirect('no_access')

@login_required(login_url='/login/')
def profile_show(request):
    # vehicles = Vehicle(user=request.user)
    vehicles = Vehicle.objects.filter(user_id=request.user.id)
    if request.user.is_authenticated:
    # Do something for authenticated users.
        return render(request, 'profile.html', {'vehicles' : vehicles})
    else:
        return HttpResponse('<h1>Something went wrong with login</h1>')
        
def vehicle_delete(request, pk):
    if request.user.is_authenticated:
        vehicle=Vehicle.objects.get(pk=pk)
        if vehicle.user == request.user:
            vehicle.delete()
            return redirect('profile')
        else:
            return redirect('no_access')

def no_access(request):
    return render(request, 'noaccess.html')

def display(request):
    querystring = request.GET.get('VIN')
    print(querystring, 'querystring test')
    # querystring = {"vin":"WBA53BH03MWX29672"}
    url = f"https://cis-vin-decoder.p.rapidapi.com/vinDecode"
    print(url)

    headers = {
	"X-RapidAPI-Key": "3c7019782cmsh543dfafbdcda7cbp11c5a2jsn177cb39c544a",
	"X-RapidAPI-Host": "cis-vin-decoder.p.rapidapi.com"
}
    response = requests.get(url, headers=headers, params={"vin":querystring})
    info = response.text
    print(response)
    info_json = json.loads(info)
    return render(request, 'display.html', info_json)

def add_vehicle(request):
    print('is it hitting the route?')
    if request.method == 'POST':
        print('whats not working?')
        form = VehicleForm(request.POST)
        print(form)
        if form.is_valid():
            print('let meknow where')
            form.instance.user = request.user
            if not Vehicle.objects.filter(vin=request.POST.get('vin')).exists():
                vehicle = form.save()
                return redirect('profile')
            else:
                return render(request, 'display.html', {'msg': 'This VIN already exists in your profile'})
    else:
        print('is this here?')
        form = VehicleForm()
    context = {'form': form, 'header': 'Add Vehicle in your profile.', 'msg': ''}
    print('is this working?')
    return render(request, 'display.html', context)
    # Vehicle.objects.create(make = request.POST.get('make'),
    #                         vin = request.POST.get('vin'),
    #                         model = request.POST.get('model'),
    #                         year = request.POST.get('year'),
    #                         bodyClass = request.POST.get('bodyClass')
    
    # )
    # if request.method == 'POST':
    #     print(request.POST)
    #     if request.POST.get("OK"):
    #         form = VehicleForm(request.POST)
    #         print(form, 'this is the form')
    #         if form.is_valid:
    #             form.instance.user = request.user
    #             vehicle = form.save()
    #             print(vehicle, 'vehicle form')
    #             return redirect('profile')
    #     else:
    #         print('not valid?')
    #         form = VehicleForm()
    # context = {'form': form, 'header': 'Add vehicle information'}
    # return render(request, 'display.html', context)
    # print(request, 'difjaodijfoadjfo;adjfoadjf')
    # return redirect('profile')