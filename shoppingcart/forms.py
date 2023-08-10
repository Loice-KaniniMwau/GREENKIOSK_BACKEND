from django import forms
from .models import ShoppingCart

class CartUploadForm(forms.ModelForm):
     class Meta:
        model=ShoppingCart
        fields="__all__"
        
class AddToCartForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1)