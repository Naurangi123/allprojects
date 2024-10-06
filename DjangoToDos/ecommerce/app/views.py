from django.shortcuts import render

# Create your views here.

def main(request):
    names=['Random', 'Rakul','Domain','X-User-Name']
    
    return render(request, 'index.html',{'names':names})

def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')