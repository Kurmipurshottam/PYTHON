from django.shortcuts import render
from .models import *

# Create your views here.
def login(request):
    print("==================>>>>>>>>>>>>>>>>.")
    if request.POST:
        print("=====>>>>>page load")
        user_name=request.POST['name']
        print("===>>>",user_name)
        email=request.POST['email']
        print("===>>>",email)
        password=request.POST['password']
        print("===>>>",password)
        user=User.objects.create(
            username=user_name,
            email=email,
            password=password
        )
        user.save()
        return render(request,"my_app/login.html")
    else:
        return render(request,"my_app/signup.html")

def signup(request):
    return render(request,"my_app/signup.html")

def forget_password(request):
    return render(request,"my_app/forget-password.html")