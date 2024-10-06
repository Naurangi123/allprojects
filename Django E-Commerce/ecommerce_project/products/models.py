from django.db import models
from users.models import User



class Category(models.Model):
    cat_name = models.CharField(max_length=255)
    cat_description = models.TextField()

    def __str__(self):
        return self.cat_name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    image = models.ImageField(upload_to='product_img', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    def __str__(self):
        return self.name



class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="reviews")
    rating = models.PositiveIntegerField(default=0) 
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Review for {self.product.name} by {self.user.username}'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_img')

    def __str__(self):
        return f"{self.product.name} Image"

