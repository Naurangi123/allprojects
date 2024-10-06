from . import views
from django.urls import path

urlpatterns=[
    path('',views.set_session,name="set"),
    path('get/',views.get_session,name="get"),
]