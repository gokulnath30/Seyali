from django.http.response import JsonResponse
from .models import *
import os

def preview(request):
    pass    

    # return json.loads(request.)


def get_images(request):
    if request.method == 'GET':
        inx = int(request.GET['inx'])
        img = eval(Project.objects.filter(project_name='checker')[0].imag_path)
        try:
            return JsonResponse({'pname':'checker','img_len':len(img),'img_path':img[inx],'img_name':img[inx].split('/')[-1]})
        except:
            return JsonResponse({'res':'image not found'})
    else:
        return JsonResponse({'res':'faild'})

import cv2 
def start_magic(request):
    if request.method == 'POST':
        for img,data in eval(request.POST['req'])['checker'].items():
            BASE_DIR = os.path.dirname(os.path.dirname(__file__))
            impath = os.path.join(BASE_DIR,'tool/static/uploads/checker/',img)
            img =cv2.imread(impath)
            for cls in data:
                for c,obj in cls.items():
                    
                    print(impath,c,obj,img.shape)

                    cv2.rectangle(img, (int(obj[0]), int(obj[1])), (int(obj[2]),int(obj[3])), (255,0,0), 2)
            cv2.imshow('img',img)
            cv2.waitKey(0)
        return JsonResponse({'res':'here'})
    else:
        return JsonResponse({'res':'faild'})

