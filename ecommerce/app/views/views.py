from django.shortcuts import render
from ..models import *
# Create your views here.

def index(request):
    request.session['order_items'] = []
    request.session['total_items_count'] = 0
    if 'order_items' not in request.session:
        request.session['order_items'] = []
    return render(request, "index.html", {
        "products": Product.objects.all(),
        'order_items': request.session['order_items']
    })

def cart(request):
    session_id = request.session.session_key
    order_items = OrderItem.objects.filter(user_session=session_id)
    item_totals = [ item.product_amount * item.product_price for item in order_items]
    cart_total = sum(item_totals)
    order_items_with_total = []
    for item in order_items:
        order_items_with_total.append({
            "item": item,
            "item_total_price": item.product_price * item.product_amount
        })
        
   
    return render(request, "cart.html", {
        "order_items":  order_items_with_total,
        "item_totals": item_totals,
        "cart_total": cart_total
        
    })

def after_purchase(request):
    session_id = request.session.session_key
    order_items = OrderItem.objects.filter(user_session=session_id)
    delivery_adress = User_Adress.objects.filter(user_session=session_id).order_by('-created_at').first()

    total_each_item = [item.product_amount * item.product_price for item in order_items]
    total_order_price = sum(total_each_item)
    
    print(f"TOTAL EACH ITEM LIST: {total_each_item}")
    print(f"TOTAL : {total_order_price}")
    
    
    return render(request, "after_purchase.html", {
        "total_order_price" : total_order_price,
        "order_items": order_items,
        "delivery_adress": delivery_adress
        
    })
