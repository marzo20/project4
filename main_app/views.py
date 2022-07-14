from xmlrpc.client import ResponseError
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


#Define the home view
def home(request):
    return HttpResponse('<h1>Niche Market<h1>')

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