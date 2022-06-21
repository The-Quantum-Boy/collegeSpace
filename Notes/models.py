from distutils.command.upload import upload
from urllib import request
from django.db import models
from django.forms import FileField
from django.contrib.auth.models import User

class Note(models.Model):
    title=models.CharField(max_length=50)
    pdf=models.FileField(upload_to='static/pdf/',null=True)
    def __str__(request):
        return request.title

class testapp_user(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    real_name=models.CharField(max_length=50)
    def __str__(request):
        return request.real_name
        
class subject(models.Model):
    title=models.CharField(max_length=100)
    pdf=models.FileField(upload_to='static/pdf/',null=True)
    def __str__(request):
        return request.title
        