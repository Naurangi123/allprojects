from django.urls import path

from .views import (EmployeeDelete,EmployeeDetail,EmployeeInsert,EmployeeList,EmployeeUpdate)




urlpatterns = [
    path('', EmployeeList.as_view(), name='EmployeeList'),
    path('<int:id>/', EmployeeDetail.as_view(), name='EmployeeDetail'),
    path('<int:id>/update/', EmployeeUpdate.as_view(), name='EmployeeUpdate'),
    path('<int:id>/delete/', EmployeeDelete.as_view(), name='EmployeeDelete'),
    path('add/', EmployeeInsert.as_view(), name='EmployeeInsert'),
]
