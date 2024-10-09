from django.urls import path
from . import views

urlpatterns=[
    
    path('',views.addProduct,name="addProduct"),
    path('product/',views.products,name="product"),
]