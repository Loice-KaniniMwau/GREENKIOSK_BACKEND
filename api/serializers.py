from rest_framework import serializers
from customer.models import Customer
from inventory.models import Product
from shoppingcart.models import Product_Cart
from order.models import Order
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields="__all__"


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields="__all__"

class ShoppingCartSerializer(serializers.ModelSerializer):
      class Meta:
        model=Product_Cart
        fields="__all__"
