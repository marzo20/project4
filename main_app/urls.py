from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_request, name='login_page'),
    path('profile/', views.profile_show, name='profile'),
    path('logout/', views.logout_request, name='logout'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('vehicles/add/', views.vehicle_create, name='vehicle_add'),
    path('vehicles/<int:pk>/edit', views.vehicle_edit, name='vehicle_edit'),
    path('vehicles/<int:pk>/delete', views.vehicle_delete, name='vehicle_delete'),
    path('register/', views.register_request, name="register"),
    path('info/', views.info, name='info'),
    path('info/details/', views.index, name='details'),
    path('profile/add/', views.display, name='display'),
    path('profile/add/create/', views.add_vehicle, name="add_vehicle"),
    path('about/', views.about, name='about'),
]