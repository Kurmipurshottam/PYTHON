from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,"team/home.html")

def rcb(request):
	return render(request,"team/rcb.html")

def kkr(request):
	return render(request,"team/kkr.html")

def csk(request):
	return render(request,"team/csk.html")

def mi(request):
	return render(request,"team/mi.html")

def rr(request):
	return render(request,"team/rr.html")

def srh(request):
	return render(request,"team/srh.html")

def dc(request):
	return render(request,"team/dc.html")

def gt(request):
	return render(request,"team/gt.html")

def lsg(request):
	return render(request,"team/lsg.html")
	
def pbsk(request):
	return render(request,"team/pbsk.html")

