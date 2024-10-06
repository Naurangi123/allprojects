from django.urls import path
from . .api import views


urlpatterns=[
    path('',views.movie_list,name='movies'),
    path('movie/<int:pk>/',views.movie_details,name='movie'),
]