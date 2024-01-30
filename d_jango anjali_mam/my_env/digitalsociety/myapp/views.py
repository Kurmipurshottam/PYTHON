from django.shortcuts import render, HttpResponseRedirect
from .models import *
from django.urls import reverse
import random
# from .utils import *

# Create your views here.
def home(request):
    if "email" in request.session:
        uid=User.objects.get(email = request.session['email'])
        cid=Chairman.objects.get(userid = uid)
        context={
                'uid' : uid,
                'cid' : cid,
            }
        return render(request,"myapp/index.html",context)
    else:
        return render(request,"myapp/login.html")

def login(request):
    if "email" in request.session:
        # ::long code::
        # uid=User.objects.get(email = request.session['email'])
        # cid=Chairman.objects.get(userid = uid)
        # context={
        #         'uid' : uid,
        #         'cid' : cid,
        #     }
        # return render(request,"myapp/index.html",context)
        # ::short code::
        return HttpResponseRedirect(reverse("home"))
    else:
        if request.POST:
            try:
                p_email=request.POST["email"]
                p_password=request.POST["password"]
                print("======>>>",p_email)
                uid=User.objects.get(email=p_email,password=p_password)
                print("===>>>",uid)
                print("===>>>",uid.email)
                print("===>>>",uid.role)
                cid=Chairman.objects.get(userid=uid)
                print("=>name",cid.firstname+cid.lasttname)

                request.session['email'] = uid.email
                #::long code::
                #return render(request,"myapp/login.html")
                # context={
                #     'uid' : uid,
                #     'cid' : cid,
                # }
                # return render(request,"myapp/index.html",context)
                #::short code::
                return HttpResponseRedirect(reverse("home"))
            except Exception as e:
                print("==>>e",e)
                msg="please enter valid email or password"
                return render(request,"myapp/login.html",{'e_msg':msg})
                pass
        else:
            print("==>>page load")
            return render(request,"myapp/login.html")
def logout(request):
    if "email" in request.session:
        del request.session['email']
        return HttpResponseRedirect(reverse("login"))
    else:
        return HttpResponseRedirect(reverse("login"))
    
def profile(request):
    if "email" in request.session:
        uid=User.objects.get(email = request.session['email'])
        cid=Chairman.objects.get(userid = uid)
        context={
                'uid' : uid,
                'cid' : cid,
            }
        return render(request,"myapp/profile.html",context)
    else:
        return HttpResponseRedirect(reverse("login"))

def change_password(request):
    if "email" in request.session:
        uid=User.objects.get(email = request.session['email'])
        cid=Chairman.objects.get(userid = uid)

        currentpassword = request.POST['currentpassword']
        newpassword = request.POST['newpassword']

        if uid.password == currentpassword:
            uid.password = newpassword
            uid.save() #update
            del request.session['email']
            s_msg="Password changed succesfully"
            return render(request,"myapp/login.html",{'s_msg':s_msg})   
        else:
            e_msg="Invalid current password"
            del request.session['email']
            return render(request,"myapp/login.html",{'e_msg':e_msg})
        
def change_profile(request):
    if "email" in request.session:
        uid=User.objects.get(email = request.session['email'])
        cid=Chairman.objects.get(userid = uid)
        
        if request.POST:
            cid.firstname = request.POST['firstname']
            cid.lasttname = request.POST['lasttname']
            cid.contact = request.POST['contact']
            cid.blockno = request.POST['blockno']
            cid.houseno = request.POST['houseno']
            if "pic" in request.FILES:
                cid.pic = request.FILES['pic']
            cid.save()#update
        context={
                    'uid' : uid,
                    'cid' : cid,
                }
        return render(request,"myapp/profile.html",context)  
    
def add_member(request):
    if "email" in request.session:
        uid=User.objects.get(email = request.session['email'])
        cid=Chairman.objects.get(userid = uid)
        if request.POST:
            print("---->add operation")
            email=request.POST['email']
            contact=request.POST['contact']
            firstname=request.POST['firstname'],
            password=email[3:6]+contact[5:9]+email[0:3]+contact[0:4]
            muid=User.objects.create(email = request.POST['email'],password=password,role="member")
            if muid:
                print("page load =========================================>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.")
                mid=Member.objects.create(
                    userid=muid,
                    firstname=request.POST['firstname'],
                    lasttname=request.POST['lasttname'],
                    contact = request.POST['contact'],
                    blockno=request.POST['block_no'],
                    houseno=request.POST['house_no'],
                    occupation=request.POST['occupation'],
                    job_address=request.POST['job_address'],
                    bloodgroup=request.POST['blood_group'],
                    vehical_details=request.POST['vehical_details'],
                )
                # if mid:
                #     mymailfunction("welcome to digital society","mymailtemplate",email,{'firstname' : firstname,'password' : password})
                context={
                        'uid' : uid,
                        'cid' : cid,
                        's_msg' : "successfully Member added"
                }
                return render(request,"myapp/add_member.html",context)
        context={
                        'uid' : uid,
                        'cid' : cid,
                    }
        return render(request,"myapp/add_member.html",context)