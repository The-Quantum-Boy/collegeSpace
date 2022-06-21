from django.shortcuts import render
from contactus.models import *

def Contactus(request):
    return render(request,'contactus/Contact Us.html')

def msgsend(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        c=contactmsg()
        c.name=name
        c.email=email
        c.msg=message
        c.save()
        data={'msg_name':name}
        return render(request,'contactus/Contact Us.html',data)