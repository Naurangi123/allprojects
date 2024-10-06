
from django.urls import path
from . import views
from .views import StudentView


urlpatterns = [
    # path('', views.save,name="student"),
    path('',StudentView.as_view(),name='student'),
]