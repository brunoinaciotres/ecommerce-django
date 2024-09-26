from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)

    def __str__(self):
        return f"ID {self.id} - {self.name}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.FloatField()
    stock = models.IntegerField()
    def __str__(self):
        return f"ID {self.id} - {self.name}"


class Cart(models.Model):
    total_price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    def __str__(self):
        return f"ID {self.id} - Carrinho de {self.user.name}"
    

class OrderItem(models.Model):
    product_amount = models.IntegerField()
    total_item_price = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    def __str__(self):
        return f"ID {self.id} - {self.product_amount}x {self.product.name} - R${self.total_item_price} "