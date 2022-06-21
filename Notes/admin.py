from django.contrib import admin

from Notes.models import Note, testapp_user,subject

admin.site.register(Note)
admin.site.register(testapp_user)
admin.site.register(subject)