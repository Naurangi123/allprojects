from typing import Any
from django.db.models.query import QuerySet
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView,UpdateView,CreateView
from django.shortcuts import render
from .models import Book
from .forms import BookForm
# Create your views here.



class BookView(ListView):
    
    model=Book
    template_name="index.html"
    
    def get_queryset(self,*args,**kwargs):
        
        qs=super(BookView,self).get_queryset(*args,**kwargs)
        qs=qs.order_by('-id')
        return qs
    
class DetailsView(DetailView):
    
    model=Book
    template_name="detail.html"
    
class UpdatedView(UpdateView):
    
    model=Book
    template_name="update.html"
    fields=['title','name','price']
    success_url='/'
    
class DeletedView(DeleteView):
    model=Book
    template_name="delete.html"
    success_url='/'
    
class CreatedView(CreateView):
    model=Book
    template_name='create.html'
    fields=['title','name','price']
    success_url='/'