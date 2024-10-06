from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    fname=forms.CharField(label="First Name")
    lname=forms.CharField(label="Last Name")
    date_of_addmissin=forms.CharField(label="Date of Addmission")
    course=forms.CharField(label="Course")
    userid=forms.CharField(label="User Name")
    password=forms.CharField(label="Password",widget=forms.PasswordInput)
    
    class Meta:
        model=Student
        fields='__all__'