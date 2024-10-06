from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('login/',views.loginInfo,name="login"),
    path('forgetpassword/',views.forgetPassword,name="forgetpassword"),
    path('register/',views.register,name="register"),
]