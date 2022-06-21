from django.urls import path
from Quepaper.views import *

urlpatterns=[
     path('quepaper/',Question_Paper),
     path('sem1/',Firstsem1),
     path('sem2/',Firstsem2),
     path('sem3/',Secondsem3),
     path('sem4/',Secondsem4),
     path('sem5/',Thirdsem5),
     path('sem6/',Thirdsem6),
     path('back/',back),
]