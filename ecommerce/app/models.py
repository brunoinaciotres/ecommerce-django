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
        return f"{self.name} - R${self.price:.2f}"


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_total_price(self):
        total = sum(item.product.price * item.product_amount for item in self.order_items.all())

        return total

    def __str__(self):
        return f"Order {self.id}"

class OrderItem(models.Model):
    STATUS_CHOICES = [
        ('aberto', 'Aberto'),
        ('fechado', 'Fechado'),
    ]

    product_amount = models.IntegerField()
    product_price = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="order_items", blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items", null=True, blank=True)
    user_session = models.CharField(max_length=200)
    
    def __str__(self):
        return f"ID {self.id} - {self.product.name} ( {self.product_amount}un )  "


class Payment(models.Model):
    method = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField()
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)

class User_Payment_Card(models.Model):
    method = models.CharField(max_length=30, null=False)
    card_number = models.CharField(max_length=20,null=False)
    owner_name = models.CharField(max_length=200,null=False)
    cvc = models.CharField(max_length=3,null=False)
    expires_at = models.DateField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,  blank=True, null=True)
    user_session = models.CharField(max_length=200)
    
class User_Adress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  blank=True, null=True)
    user_session = models.CharField(max_length=200)
    street = models.CharField(max_length=200, null=False, blank=False)
    number = models.CharField(max_length=200, null=False, blank=False)
    complement = models.CharField(max_length=200, null=True, blank=True)
    district = models.CharField(max_length=200, null=False, blank=False)
    state = models.CharField(max_length=150, null=False, blank=False)
    city = models.CharField(max_length=150, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['street', 'number', 'complement', 'district', 'state', 'city'],
                name='unique_address_constraint'
            )
        ]
    

class Rating(models.Model):
    content = models.CharField(max_length=300)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="ratings")



