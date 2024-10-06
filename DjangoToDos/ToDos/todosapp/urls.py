from django.urls import path
from . import views


urlpatterns=[
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logoutuser,name='logoutuser'),
    path('login/',views.loginuser,name='loginuser'),
    path('todos/',views.currenttodo,name='currenttodo'),
    path('completed/',views.completedtodos,name='completedtodos'),
    path('createtodo/',views.createtodo,name='createtodo'),
    path('delete/<int:todo_id>/',views.deletetodo,name='deletetodo'),
    path('update_view/<int:todo_id>/',views.view_updatetodo,name='view_updatetodo'),
    path('update_view/<int:todo_id>/complete/',views.completetodo,name='completetodo'),
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
]

