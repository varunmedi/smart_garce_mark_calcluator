from django.db import models
from django.contrib.auth.models import User,auth
from django.contrib.auth.models import (
    AbstractBaseUser,BaseUserManager
)
# Create your models here.
class Faculty(models.Model): 
       img=models.ImageField(upload_to='pics')
       about=models.CharField(max_length=150)
       name=models.CharField(max_length=50)
       email=models.EmailField(verbose_name="email",max_length=50,unique=True,primary_key=True)
       password=models.CharField(max_length=10,verbose_name="password")
       role=models.CharField(max_length=50)
       teaches=models.CharField(max_length=50)
       phone=models.CharField(max_length=12)
       url=models.URLField(max_length=200)
       street=models.CharField(max_length=50)
       city=models.CharField(max_length=50)
       state=models.CharField(max_length=50)
       zipcode=models.CharField(max_length=50)
       
      

class Student(models.Model): 
       name=models.CharField(max_length=50)
       roll=models.CharField(max_length=50,primary_key=True)
       password=models.CharField(max_length=10,verbose_name="password")
       img=models.ImageField(upload_to='pics')
       branch = models.CharField(max_length=5)
       year=models.IntegerField()
       grace=models.IntegerField()
       grade=models.CharField(max_length=2)
       marks=models.TextField()
class Subjects(models.Model):
       branch=models.CharField(max_length=5)
       year=models.IntegerField()
       subj=models.TextField() 

