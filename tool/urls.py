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
    

    path('upload_dataset',upload_dataset),

    ]