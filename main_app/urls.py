from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login_page'),
    path('profile/', views.profile_show, name='profile'),
    path('logout/', views.logout_view, name='logout'),
]