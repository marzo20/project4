from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_request, name='login_page'),
    path('profile/', views.profile_show, name='profile'),
    path('logout/', views.logout_request, name='logout'),
    path('posts/', views.posts, name='posts'),
    path('posts/add/', views.post_create, name='post_add'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/<int:pk>/edit/', views.vehicle_edit, name='vehicle_edit'),
    path('posts/<int:pk>/delete/', views.vehicle_delete, name='vehicle_delete'),
    path('register/', views.register_request, name="register"),
    path('info/', views.info, name='info'),
    path('info/details/', views.index, name='details'),
    path('profile/add/', views.display, name='display'),
    path('profile/add/create/', views.add_vehicle, name="add_vehicle"),
    path('about/', views.about, name='about'),
]