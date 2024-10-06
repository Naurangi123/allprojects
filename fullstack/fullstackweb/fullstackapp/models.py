from django.db import models

# Create your models here.

class Department(models.Model):
    
    DeptName=models.CharField(max_length=30)
    LocationName=models.CharField(max_length=30)
    
    
    def __str__(self):
        return self.DeptName
    
    
    class Meta:
        db_table='Department'
        

class Country(models.Model):
    
    CountryName=models.CharField(max_length=30)
    
    
    def __str__(self):
        return self.CountryName
    
    
    class Meta:
        db_table='Country'    
        

class Employee(models.Model):
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    TitleName=models.CharField(max_length=30)
    HasPassport=models.BooleanField()
    Salary=models.IntegerField()
    BirthDate=models.DateField()
    HireDate=models.DateField()
    Notes=models.CharField(max_length=30)
    Email=models.EmailField(default="",max_length=50)
    PhoneNumber=models.CharField(default="",max_length=30)
    EmpDepartment=models.ForeignKey("Department",default=0,on_delete=models.PROTECT)
    EmpCountry=models.ForeignKey("Country",default=0,on_delete=models.PROTECT)    

    class Meta:
        db_table="Employee"