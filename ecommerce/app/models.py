import datetime
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.FloatField()
    stock = models.IntegerField()
    def __str__(self):
        return f"ID {self.id} - {self.name}"
    
class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField()
    
class OrderItem(models.Model):
    product_amount = models.IntegerField()
    product_price = models.FloatField(null=True, blank=True)
    status = models.CharField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')  
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="order-items")  
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order-items", null=True, blank=True)
    def __str__(self):
        return f"Id {self.id} - {self.product.name} - x{self.total_amount} "

class Payment(models.Model):
    method = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField()
    order = models.OneToOneField(Order, primary_key=True, on_delete=models.DO_NOTHING)    
    

class Rating(models.Model):
    content = models.CharField(max_length=300)
    rating = models.IntegerField()
    created_at: models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="ratings")


