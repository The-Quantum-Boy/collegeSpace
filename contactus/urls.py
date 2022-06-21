from urllib import request
from django.urls import path
from contactus.views import *

urlpatterns = [
   path('contact/',Contactus),
   path('Mail/',msgsend),
]