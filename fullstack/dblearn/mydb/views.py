from django.shortcuts import render
from django.views import View
from .forms import StudentForm

# Create your views here.

class StudentView(View):
    def get(self,request):
        
        form=StudentForm()
        context={
            'form':form,
        }
        return render(request,'index.html',context)
    
    def post(self,request):
        if request.method=='POST':
            form=StudentForm(request.POST)
            if form.is_valid():
                new_form=form.save(commit=False)
                new_form.save()
            return render(request,'welcome.html')   
        else:
            form=StudentForm()
        return render(request,'index.html',{'form':form})     
        

# def save(request):
#     if request.method=='POST':
#         form=StudentForm(request.POST)
#         if form.is_valid():
#             form.save()   
#         return render(request,'welcome.html')
#     else:
#         form=StudentForm()
#     return render(request,'index.html',{'form':form})   