from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from .models import Employee
from .forms import EmployeeForm  

# Create your views here.

class EmployeeList(View):
    def get(self, request, *args, **kwargs):
        employees = Employee.objects.select_related('EmpDepartment', 'EmpCountry').all()
        template_file = "fullstackapp/EmployeeList.html"
        context = {
            'employees': employees, 
        }
        return render(request, template_file, context)

class EmployeeDetail(View):
    def get(self, request, id, *args, **kwargs):
        employee = get_object_or_404(Employee, id=id)  
        template_file = "fullstackapp/EmployeeDetails.html"
        context = {
            'employee': employee,
        }
        return render(request, template_file, context)

class EmployeeDelete(View):
    def get(self, request, id, *args, **kwargs):
        employee = get_object_or_404(Employee, id=id)  
        template_file = "fullstackapp/EmployeeDelete.html"
        context = {
            'employee': employee,
        }
        return render(request, template_file, context)

    def post(self, request, id, *args, **kwargs):
        employee = get_object_or_404(Employee, id=id)  
        employee.delete()  
        return redirect("EmployeeList")

class EmployeeUpdate(View):
    def get(self, request, id, *args, **kwargs):
        employee = get_object_or_404(Employee, id=id)  
        template_file = "fullstackapp/EmployeeUpdate.html"
        form = EmployeeForm(instance=employee)
        context = {
            'form': form,
        }
        return render(request, template_file, context)

    def post(self, request, id, *args, **kwargs):
        employee = get_object_or_404(Employee, id=id) 
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("EmployeeList")
        template_file = "fullstackapp/EmployeeUpdate.html"
        context = {
            'form': form,
        }
        return render(request, template_file, context)

class EmployeeInsert(View):
    def get(self, request, *args, **kwargs):
        template_file = "fullstackapp/EmployeeInsert.html"
        form = EmployeeForm()
        context = {
            'form': form,
        }
        return render(request, template_file, context)

    def post(self, request, *args, **kwargs):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("EmployeeList")
        template_file = "fullstackapp/EmployeeInsert.html"
        context = {
            'form': form,
        }
        return render(request, template_file, context)
