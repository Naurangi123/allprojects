from django.shortcuts import render,redirect
from .forms import *

# Create your views here.

def register(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            username=request.POST=['userid']
            if Student.objects.filter(userid=username):
                raise forms.ValidationError('User already Exist!.')
            form.save()
            return redirect('/success')
    else:
        form=StudentForm()
    return render(request,'myapp/register.html',{'stu':form})

def success(request):
    return render(request,'myapp/success.html')


def login(request):
    if request.method=='POST':
        username=request.POST['userid']
        password=request.POST['password']
        try:
            record=Student.objects.get(userid=username,password=password)
            if record is not None:
                return redirect('/logsuccess')
            else:
                return redirect('/invalid')
        except:
            return redirect('/invalid')
    else:
        form=StudentForm()
    return render(request,'myapp/login.html',{'stu':form})

def logsuc(request):
    return render(request,'myapp/loginsuccess.html')

def loginvalid(request):
    return render(request,'myapp/invalid.html')