from django.urls import path
from . import views

urlpatterns =[
    path('',views.main,name="index"),
    path('login/',views.login,name="login"),
    path('home/',views.home,name="home"),
]