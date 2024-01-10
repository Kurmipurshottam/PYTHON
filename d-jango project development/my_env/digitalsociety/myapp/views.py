from django.shortcuts import render, HttpResponseRedirect
from .models import *
from django.urls import reverse

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
