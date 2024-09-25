from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.FloatField()
    stock = models.IntegerField()

class OrderItem(models.Model):
    product_amount = models.IntegerField()
    total_item_price = models.FloatField()
    product_id = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name='products')
class Cart(models.Model):
    total_price = models.FloatField()
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    #order_item_id = models.ForeignKey(orderItem, on_delete=models.PROTECT, related_name='items')




