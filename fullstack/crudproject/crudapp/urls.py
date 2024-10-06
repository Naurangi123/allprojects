
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path('show/',views.show,name='show'),
    path('edit/<int:id>/', views.edit_emp, name='edit'),
    path('delete/<int:id>/', views.delete_emp, name='delete'),
]
