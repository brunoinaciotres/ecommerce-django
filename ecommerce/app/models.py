import datetime
from typing import List
from django.db import models

class Cart(models.Model):
    total_price = models.FloatField()
    
    def __str__(self):
        return f"ID {self.id}"
    

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)
    cart = models.ForeignKey(Cart, blank=True, on_delete=models.DO_NOTHING, related_name="user")
    def __str__(self):
        return f"ID {self.id} - {self.name}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.FloatField()
    stock = models.IntegerField()
    def __str__(self):
        return f"ID {self.id} - {self.name}"
    

    
class OrderItem(models.Model):
    product_amount = models.IntegerField()
    total_item_price = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')    
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="order_items")
    def __str__(self):
        return f"Id {self.id} - {self.product.name} - R${self.total_item_price} "


class Order(models.Model):
    created_at: datetime = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField()
    cart = models.OneToOneField(Cart, primary_key=True, on_delete=models.DO_NOTHING)

class Payment(models.Model):
    method: int = models.IntegerField()
    created_at: datetime = models.DateTimeField(auto_now_add=True)
    updated_at: datetime = models.DateTimeField(auto_now=True)
    status: str = models.CharField(max_length=30)
    price_in_cents: float = models.FloatField()
    pedido: int = models.OneToOneField(Order, primary_key=True, on_delete=models.DO_NOTHING)    


