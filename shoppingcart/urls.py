from django.urls import path

from .views import view_cart
from .views import add_to_cart
from .views import update_cart
from .views import remove_item
from .views import empty_cart

urlpatterns=[
   
   
    path('add_to_cart/<int:id>/', add_to_cart, name='add_to_cart'),
    path('product_cart/', view_cart, name='view_cart'),
    path('update_cart/<int:id>/',update_cart, name='update_cart'),
    path("remove_item/<int:id>/", remove_item, name = "remove_item"),
    path("empty/", empty_cart, name="empty_cart"),
   
]
