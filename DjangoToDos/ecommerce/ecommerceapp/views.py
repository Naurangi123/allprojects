from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'ecommerce/index.html')

def loginInfo(request):
    return render(request, 'ecommerce/login.html')

def forgetPassword(request):
    
    return render(request, 'ecommerce/forgot_password.html')

def register(request):
    return render(request, 'ecommerce/register.html')