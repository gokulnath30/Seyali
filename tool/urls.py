from django.contrib import admin
from django.urls import path
from tool import views
urlpatterns = [
    path('', views.index),
    path('signpage/', views.signpage),
    path('add_user',views.add_user),
    ]