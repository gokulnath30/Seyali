from django.shortcuts import render
from django.http.response import JsonResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth.hashers import make_password

def index(request):
    return render(request, ('index.html'))  

def signpage(request):
    return render(request, ('sign.html'))

def home(request):
    return render(request, ('home.html'))


def add_user(request):
    if request.method == 'POST':
        if len(User.objects.filter(email=request.POST['email'])) == 0:
            User.objects.create(username = request.POST['fname'],email=request.POST['email'],password=make_password(request.POST['password']))
            return JsonResponse({"res":"success"})
        else:
            return JsonResponse({"res":"User already Exixt"})
    else:
        return JsonResponse({"res":"faild"})
            
   

