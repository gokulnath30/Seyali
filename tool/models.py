from django.db import models

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=200,default='NA')
    imag_path = models.CharField(max_length=200, default='NA')
    owner_name = models.CharField(max_length=200, default='NA')
    members = models.CharField(max_length=500, default='NA') 
    time = models.DateTimeField(auto_now=True)

# 1  test   ['1.pmg',2.png]  gokul  ['gokul@gmail.com','test@gmail.com'] 2023:20
# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     Project_id = models.CharField(max_length=200, default='NA')
#     user = models.CharField(max_length=200, default='NA')
#     imgCount = models.CharField(max_length=200, default='NA')
#     time = models.DateTimeField(auto_now=True)

# 1 gokulnath@gmial.com  10 