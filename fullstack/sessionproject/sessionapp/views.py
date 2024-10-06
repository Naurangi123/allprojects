from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def set_session(request):
    request.session["ename"]="xyz"
    request.session["email"]="abc@gmail.com"
    return HttpResponse("Session is now set")


def get_session(request):
    empname=request.session["ename"]
    empemail=request.session["email"]
    return HttpResponse("Employee Name "+empname+" "+"Email "+empemail)
