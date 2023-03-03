from django.contrib import admin
from django.urls import path
from .views import *
from .routes import *

urlpatterns = [
    # routes 
    path('', loginpage),
    path('login', loginpage),
    path('signup',signup),
    path('home', home),

    # APIS
    path('newuser',newuser),
    path('signin',signin),
    

    path('create_project',create_project),

    ]