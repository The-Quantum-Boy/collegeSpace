import imp
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect

def syllabus(request):
    res=render(request,'Syllabus/syllabus.html')
    return res

def close(request):
    return HttpResponseRedirect('http://localhost:8000/www.HVPMcollegespace.com/')