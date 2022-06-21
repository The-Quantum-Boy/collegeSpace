from urllib import request
from django.urls import path
from Attendance.views import *

urlpatterns = [
    path('login/',Login),
    path('add_data/',add_data),
    path('signup/',signup),
    path('take_attendance/',take_attendance),
    path('save_attendance/<int:id>/<str:name>/<int:presenty>/<str:sub>/<str:date>/',save_attendance),
    path('report/',report),
    path('give_report/',give_report),
    path('save/',save),
]