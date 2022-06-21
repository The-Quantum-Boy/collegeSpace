from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from Notes.models import Note,testapp_user,subject
from django.contrib.auth import authenticate
from django.contrib.auth import login


def Delete(request,id):
    n=Note.objects.get(id=id)
    n.delete()
    notes=Note.objects.all()
    data={'notes':notes}
    return render(request,'Notes/Anotes.html',data)
   
def add_notes(request):
    notes=Note.objects.all()
    data={'notes':notes}
    return render(request,'Notes/Anotes.html',data)

def Login(request):
    res=render(request,'Notes/login.html')
    return res

def checkLogin(request):
    data={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect("http://localhost:8000/Notes/Anotes/")
        else:
            data['error']='Username or password is incorrect'
            return render(request,'Notes/login.html',data)
    else:
        return HttpResponseRedirect('http://localhost:8000/Notes/login/')

def Notes(request):
    res=render(request,'Notes/notes 1.html')
    return res

def Notes1(request):
    res=render(request,'Notes/note1.html')
    return res

def Notes2(request):
    res=render(request,'Notes/note2.html')
    return res

def Notes3(request):
    res=render(request,'Notes/note3.html')
    return res

def table(request,sub):
    s=subject.objects.filter(title__iexact=sub)
    # if s!=None:
    data={'datas':s}
    return render(request,'Notes/table.html',data)
    # else:
    #     data="<p>Sorry! Notes is not Available For this Subject</p>"
    #     return render(request,'Notes/table.html',data)
