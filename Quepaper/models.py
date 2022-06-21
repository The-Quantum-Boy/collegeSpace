from django.db import models

class sem1(models.Model):
    Title=models.CharField(max_length=50)
    pdf=models.FileField(upload_to='static/pdf/')
    def __str__(self):
        return self.Title

class sem2(models.Model):
    Title=models.CharField(max_length=50)
    pdf=models.FileField(upload_to='static/pdf/')
    def __str__(self):
        return self.Title

class sem3(models.Model):
    Title=models.CharField(max_length=50)
    pdf=models.FileField(upload_to='static/pdf/')
    def __str__(self):
        return self.Title

class sem4(models.Model):
    Title=models.CharField(max_length=50)
    pdf=models.FileField(upload_to='static/pdf/')
    def __str__(self):
        return self.Title

class sem5(models.Model):
    Title=models.CharField(max_length=50)
    pdf=models.FileField(upload_to='static/pdf/')
    def __str__(self):
        return self.Title

class sem6(models.Model):
    Title=models.CharField(max_length=50)
    pdf=models.FileField(upload_to='static/pdf/')
    def __str__(self):
        return self.Title