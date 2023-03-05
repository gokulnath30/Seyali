from django.http.response import JsonResponse
from .models import *
import os

def yoloconvertion(x1, y1, x2, y2,width_image, height_image,class_label):
   # Define the coordinates and class label
    # x1, y1, x2, y2, _, class_label = (207, 113, 380, 252, 650, 650, 0)

    # Calculate the center_x, center_y, width, and height
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    width = x2 - x1
    height = y2 - y1

    # Clip the width and height to a minimum of 0
    width = max(width, 0)
    height = max(height, 0)

    # Normalize the center_x and center_y to [0, 1]
    # width_image, height_image = 640, 480  # replace with the width and height of your image
    center_x /= width_image
    center_y /= height_image

    # Normalize the width and height to [0, 1]
    width /= width_image
    height /= height_image

    # Format the YOLO string
    return f"{class_label} {center_x:.6f} {center_y:.6f} {width:.6f} {height:.6f}\n"
   



def get_images(request):
    if request.method == 'GET':
        data = members.objects.filter(user=request.user)
        return JsonResponse({'pname':data[0].Project_id,'images':eval(data[0].imag_path)})

    else:
        return JsonResponse({'res':'faild'})

import cv2 
def start_magic(request):
    if request.method == 'POST':
        projectName = members.objects.filter(user=request.user)[0].Project_id
        yolo_str = ''
        for imgname,data in eval(request.POST['req']).items():
            if data:
                BASE_DIR = os.path.dirname(os.path.dirname(__file__))
                impath = os.path.join(BASE_DIR,'tool/static/uploads/'+projectName+'/',imgname)
                img =cv2.imread(impath)
                w,h,_ = img.shape
                for cls in data:
                    cls ,val = list(cls.keys())[0],list(cls.values())[0]
                    cv2.rectangle(img, (int(val[0]), int(val[1])), (int(val[2]),int(val[3])), (255,0,0), 2)
                    yolo_str += yoloconvertion(int(val[0]), int(val[1]), int(val[2]),int(val[3]) ,w,h,0)
                
                impath = 'dataset/'+projectName+'/images/'
                txtpath ='dataset/'+projectName+'/lables/'
                if not os.path.exists(impath) and not os.path.exists(txtpath):
                        os.makedirs(impath)
                        os.makedirs(txtpath)
                cv2.imwrite(impath+imgname,img)
                with open(txtpath+imgname.split('.')[0]+'.txt', 'w') as f:
                    f.write(yolo_str)

        return JsonResponse({'res':'here'})
    else:
        return JsonResponse({'res':'faild'})

