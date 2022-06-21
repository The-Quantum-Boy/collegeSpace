from django.db import models

class contactmsg(models.Model):
    name=models.CharField(max_length=80)
    email=models.EmailField()
    msg=models.CharField(max_length=400)
    def __str__(self):
        return self.name
