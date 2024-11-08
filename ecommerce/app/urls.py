from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cart", views.cart, name="cart"),
    path("add_to_cart", views.add_to_cart, name="add-to-cart"),
    path("get_user_session", views.get_user_session, name="get-user-session")
]