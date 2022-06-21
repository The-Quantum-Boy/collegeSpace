from django.urls import path
from Syllabus.views import *
urlpatterns=[
    path('syllabus/',syllabus),
    path('close/',close),
]