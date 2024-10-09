from django.db import models

# Create your models here.
class UserProfile(models.Model):
    fname = models.CharField(max_length=30)
    mname=models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    address = models.TextField()
    phone_no=models.CharField(max_length=15)
    username = models.CharField(max_length=100,primary_key=True)
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)
    
    def __str__(self):
        return self.username
    
    
    
class Product(models.Model):
    pname=models.CharField(max_length=30,null=True)
    price=models.CharField(max_length=50,null=True)
    file = models.FileField()