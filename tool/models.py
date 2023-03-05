from django.db import models

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=200,default='NA')
    classes = models.CharField(max_length=500, default='NA')
    imag_path = models.CharField(max_length=10000, default='NA')
    owner_name = models.CharField(max_length=200, default='NA')
    members = models.CharField(max_length=1000, default='NA') 
    time = models.DateTimeField(auto_now=True)

class members(models.Model):
    id = models.AutoField(primary_key=True)
    Project_id = models.CharField(max_length=200, default='NA')
    imag_path = models.CharField(max_length=10000, default='NA')
    user = models.CharField(max_length=200, default='NA')
    imgCount = models.CharField(max_length=200, default='NA')
    time = models.DateTimeField(auto_now=True)

