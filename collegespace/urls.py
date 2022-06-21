"""collegespace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import imp
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from Quepaper.urls import *
from Syllabus.urls import *
from Attendance.urls import *
from contactus.urls import *

urlpatterns = [
    path('www.HVPMcollegespace.com/',include('Home.urls')),
    path('Attendance/',include('Attendance.urls')),
    path('Quepaper/',include('Quepaper.urls')),
    path('Notes/',include('Notes.urls')),
    path('Syllabus/',include('Syllabus.urls')),
    path('admin/', admin.site.urls),
    path('Contact/',include('contactus.urls')),
]
