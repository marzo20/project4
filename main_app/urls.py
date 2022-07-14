from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login_page'),
    path('profile/', views.profile_show, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('vehicles/add/', views.vehicle_create, name='vehicle_add'),
    path('vehicles/<int:pk>/edit', views.vehicle_edit, name='vehicle_edit'),
]