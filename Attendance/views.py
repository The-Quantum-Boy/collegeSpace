from django.http import HttpResponseRedirect
from django.shortcuts import render
from Attendance.models import *
from django.contrib.auth import authenticate,login,logout
import datetime

def save(request):
    return HttpResponseRedirect('http://localhost:8000/www.HVPMcollegespace.com/')

def Login(request):
    res=render(request,'Attendance/login.html')
    return res

def report(request):
    res=render(request,'Attendance/reports.html')
    return res

def give_report(request):
    if request.method=="POST":
        sub=request.POST['subject']
        name=request.POST['name']
        if sub=='MC':
           a=Student_Data.objects.get(student_name=name)
           b=MC_Attendance.objects.filter(student_name__iexact=name)
           data={'data':b,'s':a}
           return render(request,'Attendance/reports.html',data)
        elif sub=='CGMA':
           a=Student_Data.objects.get(student_name=name)
           b=CGMA_Attendance.objects.filter(student_name__iexact=name)
           data={'data':b,'s':a}
           return render(request,'Attendance/reports.html',data)
        elif sub=='PHP':
           a=Student_Data.objects.get(student_name=name)
           b=PHP_Attendance.objects.filter(student_name__iexact=name)
           data={'data':b,'s':a}
           return render(request,'Attendance/reports.html',data)
        elif sub=='AI':
           a=Student_Data.objects.get(student_name=name)
           b=AI_Attendance.objects.filter(student_name__iexact=name)
           data={'data':b,'s':a}
           return render(request,'Attendance/reports.html',data)
    
def save_attendance(request,id,name,presenty,sub,date):
        if sub=='MC':
            a=MC_Attendance()
            a.student_name=name
            a.date=date
            a.attendance=presenty
            a.save()
            # b=MC_Attendance.objects.filter(student_name=name)
            s=Student_Data.objects.all()
            d=name
            now=datetime.datetime.now()
            x=now.strftime("%d-%m-")
            y=str(now.year)
            x+=y
            data={'data':s,'d':d,'date':x}
            return render(request,'Attendance/attendance.html',data)
        elif sub=="CGMA":
            a=CGMA_Attendance()
            a.student_name=name
            a.date=date
            a.attendance=presenty
            a.save()
            s=Student_Data.objects.all()
            d=name
            now=datetime.datetime.now()
            x=now.strftime("%d-%m-")
            y=str(now.year)
            x+=y
            data={'data':s,'d':d,'date':x}
            return render(request,'Attendance/attendance.html',data)
        elif sub=="PHP":
            a=PHP_Attendance()
            a.student_name=name
            a.date=date
            a.attendance=presenty
            a.save()
            s=Student_Data.objects.all()
            d=name
            now=datetime.datetime.now()
            x=now.strftime("%d-%m-")
            y=str(now.year)
            x+=y
            data={'data':s,'d':d,'date':x}
            return render(request,'Attendance/attendance.html',data)
        elif sub=="AI":
            a=AI_Attendance()
            a.student_name=name
            a.date=date
            a.attendance=presenty
            a.save()
            s=Student_Data.objects.all()
            d=name
            now=datetime.datetime.now()
            x=now.strftime("%d-%m-")
            y=str(now.year)
            x+=y
            data={'data':s,'d':d,'date':x}
            return render(request,'Attendance/attendance.html',data)


def take_attendance(request):
    data={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            s=Student_Data.objects.all()
            now=datetime.datetime.now()
            x=now.strftime("%d-%m-")
            y=str(now.year)
            x+=y
            data={'data':s,'date':x}
            return render(request,'Attendance/attendance.html',data)
        else:
            data['error']='Username or password is incorrect'
            return render(request,'Attendance/login.html',data)
    else:
        return HttpResponseRedirect('http://localhost:8000/Attendance/login/')
    
def add_data(request):
    res=render(request,'Attendance/add_data.html')
    return res

def signup(request):
    if request.method=='POST':
        d1=Student_Data()
        formdata=request.POST
        d1.stu_id=formdata['st_id']
        d1.student_name=formdata['st_name']
        d1.roll_no=formdata['st_rollno']
        d1.sem=formdata['st_sem']
        d1.save()
        x={'data':'Record added Successfully!'}
        return render(request,'Attendance/add_data.html',x)