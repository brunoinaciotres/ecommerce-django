from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price")

    
class RatingAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "rating", "content")

class OrderItemInline(admin.StackedInline):
    model = OrderItem
    fields = ['product_amount', 'status', 'product', 'user']
    extra = 1
    

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    readonly_fields = ['get_total_price']
    
    def get_total_price(self, obj):
        print(obj)
        return obj.get_total_price()
    
    get_total_price.short_description = 'Preço Total'
        
        

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Rating, RatingAdmin)