from django.urls import path
from Notes.views import *
urlpatterns=[
    path('login/',Login),
    path('checkLogin/',checkLogin),
    path('Anotes/',add_notes),
    path('notes/',Notes),
    path('note1/',Notes1),
    path('note2/',Notes2),
    path('note3/',Notes3),
    path('delete/<int:id>/',Delete),
    path('table/<str:sub>/',table),
]