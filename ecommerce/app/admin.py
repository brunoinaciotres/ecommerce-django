from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "cart")

class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price")

    
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "product_amount", "total_item_price")



# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Cart)
admin.site.register(Product, ProductAdmin)
admin.site.register(OrderItem, OrderItemAdmin)