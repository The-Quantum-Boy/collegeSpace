from django.db import models

class Student_Data(models.Model):
    stu_id=models.IntegerField(null=True)
    student_name=models.CharField(max_length=100)
    roll_no=models.CharField(max_length=100,null=True)
    sem=models.CharField(null=True,max_length=50)
    def __str__(self):
        return self.student_name

class CGMA_Attendance(models.Model):
    student_name=models.CharField(max_length=100)
    date=models.CharField(max_length=20,null=True)
    attendance=models.BooleanField(null=True)
    def __str__(self):
        return str(self.student_name)+" "+str(self.date)

class MC_Attendance(models.Model):
    student_name=models.CharField(max_length=100)
    date=models.CharField(max_length=20,null=True)
    attendance=models.BooleanField(null=True)
    def __str__(self):
        return str(self.student_name)+" "+str(self.date)

class AI_Attendance(models.Model):
    student_name=models.CharField(max_length=100)
    date=models.CharField(max_length=20,null=True)
    attendance=models.BooleanField(null=True)
    def __str__(self):
        return str(self.student_name)+" "+str(self.date)

class PHP_Attendance(models.Model):
    student_name=models.CharField(max_length=100)
    date=models.CharField(max_length=20,null=True)
    attendance=models.BooleanField(null=True)
    def __str__(self):
        return str(self.student_name)+" "+str(self.date)