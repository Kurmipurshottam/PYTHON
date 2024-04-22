from django.shortcuts import render
from .models import *

# Create your views here.
def login(request):
    return render(request,"my_app/login.html")

def signup(request):
    return render(request,"my_app/signup.html")

def index(request):
    return render(request,"my_app/index.html")

def forget_password(request):
    return render(request,"my_app/forget-password.html")