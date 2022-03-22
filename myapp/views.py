from pdb import post_mortem
from django.shortcuts import render
from django.http import HttpResponse
from .models import Users

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def sign(request):
    return render(request,'signup.html')

def hai(request):
    if request.method== 'POST':
        usernam=request.POST['name1']
        passwor=request.POST['name2']
        ag=request.POST['name3']
        userdata=Users(username=usernam,password=passwor,age=ag)
        userdata.save()

    return render(request,'mine.html')