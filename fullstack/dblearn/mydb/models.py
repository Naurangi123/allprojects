from django.db import models

# Create your models here.
class Student(models.Model):
    sanme=models.CharField(max_length=100)
    sclass=models.CharField(max_length=50)
    age=models.IntegerField()
    dob=models.DateField()