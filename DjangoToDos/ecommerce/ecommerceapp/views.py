from django.shortcuts import redirect, render
from .forms import UserProfileForm,ProductForm
from .functions import handle_upload
from .models import Product

# Create your views here.

def index(request):
    return render(request, 'ecommerce/index.html')

def loginInfo(request):
    return render(request, 'ecommerce/login.html')

def forgetPassword(request):
    
    return render(request, 'ecommerce/forgot_password.html')

def register(request):
    if request.method == 'POST':
        form=UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')   
    else:
        form=UserProfileForm()
    return render(request, 'ecommerce/register.html',{'form':form})


def products(request):
    products =Product.objects.all()
    count=Product.objects.count()
    return render(request, 'ecommerce/products.html', {'products': products, 'count':count})

def addProduct(request):
    if request.method == 'POST':
        img=ProductForm(request.POST, request.FILES)
        if img.is_valid():
            img.save()
            return redirect('product')   
    else:
        img=ProductForm()
    return render(request, 'ecommerce/product.html',{'img':img})


    
def middlenames(request):
    return render(request, 'ecommerce/middle.html')