"""
URL configuration for cricket_team project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from team import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rcb/', views.rcb, name='rcb'),
    path('kkr/', views.kkr, name='kkr'),
    path('csk/', views.csk, name='csk'),
    path('mi/', views.mi, name='mi'),
    path('rr/', views.rcb, name='rr'),
    path('srh/', views.kkr, name='srh'),
    path('dc/', views.csk, name='dc'),
    path('gt/', views.mi, name='gt'),
    path('lsg/', views.rcb, name='lsg'),
    path('pbsk/', views.kkr, name='pbsk'),
]
