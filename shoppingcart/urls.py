from django.urls import path

from .views import add_to_cart, view_cart, update_cart, remove_item, empty_cart,checkout_view
urlpatterns = [
    path('add_to_cart/<int:id>/', add_to_cart, name='add_to_cart'),
    path('product_cart/', view_cart, name='view_cart'),
    path('update_cart/<int:id>/',update_cart, name='update_cart'),
    path("remove_item/<int:id>/", remove_item, name = "remove_item"),
    path("empty/", empty_cart, name="empty_cart"),
    path('checkout/<int:cart_id>/', checkout_view, name='checkout'),
]
