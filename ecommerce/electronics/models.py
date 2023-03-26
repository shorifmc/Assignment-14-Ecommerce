from django.db import models

# Create your models here.

class Student (models.Model):
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=50)
    student_email = models.EmailField(max_length=35)
    batch = models.IntegerField()
    course = models.CharField(max_length=20)

class Info(models.Model): 
     first_name = models.CharField(max_length=40)
     last_name = models.CharField(max_length=40)
     email= models.EmailField(max_length=20)
     batch = models.IntegerField()
     password = models.CharField(max_length=30)
     re_password = models.CharField(max_length=30)
     textarea = models.CharField(max_length=100)
     rollno = models.IntegerField()
     payment = models.DecimalField(max_digits=6, decimal_places=2)
     django = models.BooleanField()

