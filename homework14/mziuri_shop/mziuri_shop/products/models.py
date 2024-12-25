from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models import ManyToManyField, ForeignKey


class Category(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return  self.name

class Product(models.Model):
    name = models.CharField(max_length=150, default='Product Name')
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    create_date = models.DateTimeField(default=datetime.now)
    write_time = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True, related_name='products')
    image = models.ImageField(upload_to='products/', default='default.jpg')
    stock_qty = models.IntegerField(default=0)

    def __str__(self):
        return  self.name


class CartItem(models.Model):
    product = ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    cart = ForeignKey('Cart', on_delete=models.CASCADE, related_name='cart_items')
    qty = models.IntegerField(default=1)

class Cart(models.Model):
    user = models.OneToOneField(User, related_name='cart', on_delete=models.CASCADE)