from django.db import models
from django import forms
# Create your models here.

class User(models.Model):
    FirstName=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)






