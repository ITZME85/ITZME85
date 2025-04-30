from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    email = models.CharField(max_length=90)
    doc = models.FileField(upload_to='documents/', default=0)
    img = models.ImageField(upload_to='Gallery',default=0)

class Profile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    des = models.CharField(max_length=90)

class Books(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    num = models.IntegerField()
    
class spy(models.Model):
    name = models.CharField(max_length=10)
    
