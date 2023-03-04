from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def loginpage(request):
    return render(request, ('login.html'))  

def signup(request):
    return render(request, ('signup.html'))

@login_required(login_url='/login')
def home(request):
    return render(request, ('home.html'))

@login_required(login_url='/login')
def annotate_page(request):
    return render(request, ('annotate.html'))

@login_required(login_url='/login')
def annotation(request):
    return render(request, ('annotation.html'))

