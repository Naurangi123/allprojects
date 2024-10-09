from django.db import models

# Create your models here.
class Product(models.Model):
    pname=models.CharField(max_length=30,null=True)
    price=models.CharField(max_length=50,null=True)
    file = models.FileField()