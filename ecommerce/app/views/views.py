from django.shortcuts import render
from ..models import Product
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
    return render(request, "cart.html")


