import datetime
import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

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
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=300, null=False)
    img = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    price = models.FloatField(null=False)
    stock = models.IntegerField(null=False)
    def __str__(self):
        return f"ID {self.id} - {self.name}"
    

    
class OrderItem(models.Model):
    product_amount = models.IntegerField(null=False)
    total_item_price = models.FloatField(null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')    
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="order_items")
    def __str__(self):
        return f"Id {self.id} - {self.product.name} - R${self.total_item_price} "


class Order(models.Model):
    created_at = mod
    els.DateTimeField(auto_now_add=True, null=False)
    total_price = models.FloatField(null=False)
    cart = models.OneToOneField(Cart, primary_key=True, on_delete=models.DO_NOTHING)

class Payment(models.Model):
    method = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    status = models.CharField(max_length=30, null=False)
    price_in_cents = models.FloatField(null=False)
    order = models.OneToOneField(Order, primary_key=True, on_delete=models.DO_NOTHING)    


