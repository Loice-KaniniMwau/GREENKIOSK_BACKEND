from django.urls import path

from .views import view_cart
from .views import add_to_cart
from .views import update_cart
from .views import remove_item
from .views import empty_cart

urlpatterns=[
   
   
     path('cart/add_to_cart/<int:id>/', add_to_cart, name='add_to_cart'),
     path('cart/product_cart/', view_cart, name='view_cart'),
     path('cart/update_cart/<int:id>/',update_cart, name='update_cart'),
     path("cart/remove_item/<int:id>/", remove_item, name = "remove_item"),
    path("cart/empty/", empty_cart, name="empty_cart"),
   
]
