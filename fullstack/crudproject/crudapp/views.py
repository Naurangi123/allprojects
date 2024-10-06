from django.shortcuts import redirect, render
from .forms import EmployeeForm
from .models import Employee

# Create your views here.

def index(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/show")
    else:
        form=EmployeeForm()
    return render(request,'index.html',{'form':form})


def show(request):
    employees=Employee.objects.all()
    return render(request,'show.html',{'employees':employees})

def edit_emp(request, id):
    employee=Employee.objects.get(id=id)
    print(employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/show')
    else:
        form = EmployeeForm(instance=employee)
    
    return render(request, 'update.html', {'form': form})


def delete_emp(request,id):
    employee=Employee.objects.get(id=id)
    print(employee)
    employee.delete()
    return redirect('/show')