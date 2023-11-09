from django.db import models

# Create your models here.
# models.py in the shop app

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='media/', default='profile.png') 
    # Add other fields as needed

class Category(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField
    gender = models.CharField(max_length=20)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other fields as needed

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

