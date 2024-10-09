from django.shortcuts import redirect, render
from .functions import handle_upload
from .models import Product
from .forms import ProductForm

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def addProduct(request):
    if request.method == 'POST':
        img=ProductForm(request.POST, request.FILES)
        if img.is_valid():
            img.save()
            return redirect('product')   
    else:
        img=ProductForm()
    return render(request, 'product.html',{'img':img})