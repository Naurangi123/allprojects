from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'FirstName',
            'LastName',
            'TitleName',
            'HasPassport',
            'Salary',
            'BirthDate',
            'HireDate',
            'Notes',
            'Email',
            'PhoneNumber',
            'EmpDepartment',
            'EmpCountry',
        ]
        widgets = {
            'BirthDate': forms.DateInput(attrs={'type': 'date'}),
            'HireDate': forms.DateInput(attrs={'type': 'date'}),
        }
