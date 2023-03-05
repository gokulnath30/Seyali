from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.http.response import JsonResponse, HttpResponse


def loginpage(request):
    return render(request, ('login.html'))  

def signup(request):
    return render(request, ('signup.html'))


@login_required(login_url='/login')
def home(request):
    return render(request, ('home.html'))

@login_required(login_url='/login')
def layout(request):
    return render(request, ('layout.html'))


@login_required(login_url='/login')
def annotation(request):
    return render(request, ('annotation.html'))

@login_required(login_url='/login')
# def annotate_page(request,p_name):
#     pname = Project.objects.filter(project_name = p_name)
#     print(pname[0],"...........")
#     return render(request, 'annotate.html',{"api": (pname[0].members).split(',')})

def annotate_page(request, p_name):
    pname = Project.objects.filter(project_name=p_name)
    if not pname:
        return HttpResponse('Project not found')
    else:
        api = pname[0].members.split(',')
        return render(request, 'annotate.html', {'api': api})
        


