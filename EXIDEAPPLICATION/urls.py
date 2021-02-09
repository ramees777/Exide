"""EXIDE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views
urlpatterns = [

    path('',views.home,name='home'),
    path('register',views.register_details,name='register_details'),
    path('gallery',views.gallerypage,name='gallerypage'),
    path('home',views.homepage,name='homepage'),
    path('gotohome',views.gotohome,name='gotohome'),
    path('galleryin',views.galleryin,name='galleryin'),
    path('tables',views.tables,name='tables'),
    path('purchaseinput',views.pinputpage,name='pinputpage'),
    path('login',views.login,name='login'),
    path('pdetails',views.pdetailsinput,name='pdetailsinput'),
    path('serialno',views.serialno,name='serealno'),
    path('batteryuploadpage',views.bupload,name='bupload'),
    path('bgalleryup',views.galleryup,name='galleryup'),
    path('contactpage',views.contactpage,name='contactpage'),
    path('gotohome',views.gotohome,name='gotohome'),
    path('gallerymanage',views.gallerymanage,name='gallerymanage'),
    path('retrievebdeatils',views.retrievebdeatils,name='retrievebdeatils'),
    path('retrieve',views.retrieve,name='retrieve'),
    path('stupdate',views.stupdate,name='stupdate'),
    path('gmupdate',views.gmupdate,name='gmupdate'),
    path('logoutuser',views.logoutuser,name='logoutuser'),
    path('userdetails',views.userdetails,name='userdetails'),
    path('usermanage',views.usermanage,name='usermanage'),
    path('logoutadmin',views.logoutadmin,name='logoutadmin'),

]
