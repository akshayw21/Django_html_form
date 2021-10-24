from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm

# Create your views here.

'''def home(request):
    
   
        return render(request,'home.html')'''
    
def student(request):
        return render(request,'student.html')