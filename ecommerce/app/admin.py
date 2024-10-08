from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price")

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "product_amount", "product_price")
    
class RatingAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "rating", "content")



# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Rating, RatingAdmin)