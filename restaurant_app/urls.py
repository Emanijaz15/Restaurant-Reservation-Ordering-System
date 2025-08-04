from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
  

urlpatterns = [
    path('main/', views.home, name='home'),
    path('', views.main, name='main'),
    path('menu/', views.menu, name='menu'),
    path('reserve/', views.reserve_table, name='reserve'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('contact/', views.contact, name="contact"),
    path('gallery/', views.gallery, name='gallery'),
    path('order/', views.place_order, name='place_order'),
]
 

