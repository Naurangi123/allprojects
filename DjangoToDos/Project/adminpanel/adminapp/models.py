from django.db import models

# Create your models here.
class Toys(models.Model):
    toysname=models.CharField(max_length=10)
    toyprice=models.IntegerField()
    
    def __str__(self):
        return self.toysname
    
    class Meta:
        db_table="toys"