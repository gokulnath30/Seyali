from django.http.response import JsonResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth.hashers import make_password
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render
import time
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
        # imag_path = request.POST['imag_path']
        members = request.POST['members']
        for im in  request.FILES.getlist("imag_path"):
            img = FileSystemStorage()
            img_path = 'tool/static/upload/'+project_name+'/'+ str(time.time())+'.png'
            weightsname = img.save(img_path, img)
            print(img.url(weightsname),img_path,'=======')
        # Project.objects.create(project_name = project_name, classes=classes, imag_path=imag_path, members=members)
        return JsonResponse({"res":"success"})
    else:
        return JsonResponse({"res":"faild"})            