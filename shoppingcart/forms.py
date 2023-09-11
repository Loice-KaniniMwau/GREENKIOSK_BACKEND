from django import forms
from shoppingcart.models import Product_Cart

class CartForm(forms.ModelForm):
     class Meta:
        model=Product_Cart
        fields="__all__"
        
