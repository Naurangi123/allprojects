from django.urls import path
from .views import BookView,DetailsView,UpdatedView,DeletedView,CreatedView

urlpatterns=[
    path('',BookView.as_view(),name='index'),
    path('add/',CreatedView.as_view(),name='add'),
    path('detail/<int:pk>/',DetailsView.as_view(),name='detail'),
    path('update/<int:pk>/',UpdatedView.as_view(),name='update'),
    path('delete/<int:pk>/',DeletedView.as_view(),name="delete"),
    
]