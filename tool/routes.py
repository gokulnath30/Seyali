from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def loginpage(request):
    return render(request, ('login.html'))  

def signup(request):
    return render(request, ('signup.html'))

@login_required(login_url='/login')
def home(request):
    return render(request, ('home.html'))

