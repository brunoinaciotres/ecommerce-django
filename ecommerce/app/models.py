import datetime
import uuid

from django.db import models
from django.contrib.auth.models import User

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.FloatField()
    img = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    stock = models.IntegerField()

    def __str__(self):
        return f"ID {self.id} - {self.name}"


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField()


class OrderItem(models.Model):
    product_amount = models.IntegerField()
    product_price = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="order_items")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items", null=True, blank=True)

    def __str__(self):
        return f"Id {self.id} - {self.product.name} - x{self.product_amount} "


class Payment(models.Model):
    method = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField()
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)


class Rating(models.Model):
    content = models.CharField(max_length=300)
    rating = models.IntegerField()
    created_at: models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="ratings")



