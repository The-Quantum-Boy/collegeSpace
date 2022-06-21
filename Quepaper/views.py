from django.shortcuts import render
from Quepaper.models import *
from django.http import HttpResponseRedirect

def Question_Paper(request):
    return render(request,'Quepaper/Question paper.html')

def Firstsem1(request):
    a=sem1.objects.all()
    data={'datas':a}
    return render(request,'Quepaper/First.html',data)

def Firstsem2(request):
    a=sem2.objects.all()
    data={'datas':a}
    return render(request,'Quepaper/First.html',data)

def Secondsem3(request):
    a=sem3.objects.all()
    data={'datas':a}
    return render(request,'Quepaper/First.html',data)

def Secondsem4(request):
    a=sem4.objects.all()
    data={'datas':a}
    return render(request,'Quepaper/First.html',data)

def Thirdsem5(request):
    a=sem5.objects.all()
    data={'datas':a}
    return render(request,'Quepaper/First.html',data)

def Thirdsem6(request):
    a=sem6.objects.all()
    data={'datas':a}
    return render(request,'Quepaper/First.html',data)

def back(request):
    return HttpResponseRedirect('http://localhost:8000/www.HVPMcollegespace.com/')