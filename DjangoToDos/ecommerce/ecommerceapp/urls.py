from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('login/',views.loginInfo,name="login"),
    path('forgetpassword/',views.forgetPassword,name="forgetpassword"),
    path('register/',views.register,name="register"),
    path('addProduct/',views.addProduct,name="addProduct"),
    path('product/',views.products,name="product"),
    path('middlenames/',views.middlenames,name="middlenames"),
]