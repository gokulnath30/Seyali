from django.http.response import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import FileSystemStorage
from django.db import connection
from .models import *
import uuid,os

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
                img_name = str(uuid.uuid4()).split("-")[-1]+ '.png'
                img.save(img_path+img_name, im)
                imgs.append('static/uploads/'+project_name+'/'+img_name)

            Project.objects.create(project_name=project_name, classes=request.POST['classes'], members=request.POST['members'],imag_path= imgs,owner_name = request.user)         

            return JsonResponse({'res': 'success'})
        else:
             return JsonResponse({'res': 'proejct already exist'})

    else:
        return JsonResponse({'res': 'failed'})

        


def project_details(request):
    if request.method == 'GET':
        api = []
        for x in Project.objects.all():
            if eval(x.imag_path):
                sample = eval(x.imag_path)[0]
            else:
                sample = 'static/images/download.png'
            api.append({'project':x.project_name,'count':len(eval(x.imag_path)),'sample':sample})
        return JsonResponse({"api": api})




# if os.path.isfile('tool/static/uploads/' + project_name + '/'): 
def assign_user(request):
    if request.method == 'POST':
        user = request.POST['user']
        imgCount = request.POST['imgCount']
        pro = Project.objects.filter(project_name=request.POST['project_name'])
        assgin = eval(pro[0].imag_path)[0:int(imgCount)]
        updated_rows = members.objects.filter(user=user).update(imgCount=imgCount,imag_path = assgin)
        if not updated_rows:
           members.objects.create(user=user, imgCount=imgCount,imag_path = assgin)
        
        balance = eval(pro[0].imag_path)[int(imgCount):len(pro[0].imag_path)]
        Project.objects.update(imag_path = balance)
        return JsonResponse({"res":"success"})
       
    else:
        return JsonResponse({"res":"failed"})


