from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def Insert(request):
    return render(request,'insert.html')

def Insertdata(request):
    vname = request.POST['fname']

    newuser = IVModel.objects.create(Mname=vname)

    return redirect('showdata')

def Showdata(request):
    all_data = IVModel.objects.all()
    return render(request, 'showdata.html',{'key1':all_data})



