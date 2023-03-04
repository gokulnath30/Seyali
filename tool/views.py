from django.http.response import JsonResponse
from django.core.files.storage import FileSystemStorage
import time
from django.core.files.storage import FileSystemStorage
from django.db import connection
from .models import *

def custom_sql(query):
    cursor = connection.cursor()
    cursor.execute(query)
    row = cursor.fetchall()
    connection.commit()
    connection.close()
    return row


def create_project(request):
    if request.method == 'POST':
        project_name = request.POST['project_name']
        if  len(Project.objects.filter(project_name=project_name)) == 0:
            imgs = []
            for im in request.FILES.getlist('imag_path'):
                img = FileSystemStorage()
                img_path = 'tool/static/uploads/' + project_name + '/'
                img_name = str(time.time()) + '.png'
                img.save(img_path+img_name, im)
                imgs.append('static/uploads/tests/'+project_name+'/'+img_name)

            Project.objects.create(project_name=project_name, classes=request.POST['classes'], members=request.POST['members'],imag_path= imgs,owner_name = request.user)         

            return JsonResponse({'res': 'success'})
        else:
             return JsonResponse({'res': 'proejct already exist'})

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


        