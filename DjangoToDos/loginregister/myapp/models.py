from django.db import models

# Create your models here.
class Student(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=20)
    date_of_addmissin=models.CharField(max_length=100)
    course=models.CharField(max_length=30)
    userid=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30)

    class Meta:
        db_table="student"