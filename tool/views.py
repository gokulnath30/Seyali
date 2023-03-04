from django.http.response import JsonResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth.hashers import make_password
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render
import time
from django.core.files.storage import FileSystemStorage
import os
from django.db import connection
from .models import *

def custom_sql(query):
    cursor = connection.cursor()
    cursor.execute(query)
    row = cursor.fetchall()
    connection.commit()
    connection.close()
    return row

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
            

def create_project(request):
    if request.method == 'POST':
        project_name = request.POST['project_name']
        classes = request.POST['classes']
        members = request.POST['members']
        data = Project.objects.filter(project_name=project_name) 
        
        for im in request.FILES.getlist('imag_path'):
            img = FileSystemStorage()
            img_dir = 'tool/static/upload/' + project_name
            if not os.path.exists(img_dir):
                os.makedirs(img_dir)
                
            img_path = img_dir + '/' + str(time.time()) + '.png'
            weightsname = img.save(img_path, im)
            # print(img.url(weightsname), img_path, '=======')  
            if len(data) == 0:
                Project.objects.create(project_name=project_name, classes=classes, members=[members])         
            return JsonResponse({'res': 'success'})

    else:
        return JsonResponse({'res': 'failed'})


def project_details(request):
    if request.method == 'GET':
        api = []
        for x in custom_sql("SELECT * from tool_project"):
            api.append(x)
        return JsonResponse({"api": api})


def users(request):
    if request.method == 'GET':
        api = []
        for x in custom_sql("SELECT DISTINCT members from tool_project"):
            api.append(x)
        return JsonResponse({"api": api})


        