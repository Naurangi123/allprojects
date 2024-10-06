from django.urls import path
from . import views


urlpatterns=[
    path('',views.register, name='register'),
    path('success/',views.success,name='success'),
    path('login/',views.login,name='login'),
    path('logsuccess/',views.logsuc,name='logsuccess'),
    path('invalid/',views.loginvalid,name='invalid'),
    
]