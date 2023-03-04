from django.http.response import JsonResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from .models import *


def newuser(request):
    if request.method == 'POST':
        if len(User.objects.filter(email=request.POST['email'])) == 0:
            User.objects.create(username = request.POST['username'],email=request.POST['email'],password=make_password(request.POST['password']))
            return JsonResponse({"res":"success"})
        else:
            return JsonResponse({"res":"User already Exixt"})
    else:
        return JsonResponse({"res":"faild"})
    

def signin(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return JsonResponse({'res':'sucess'})
        else:
            return JsonResponse({'res':'Invalide user name or password'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'login.html')
