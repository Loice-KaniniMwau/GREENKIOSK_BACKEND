from django.urls import path
from .views import CustomerListView,CustomerDetailView,ProductListView,ProductDetailView,OrderListView,OrderDetailView,CartListView,CartDetailView,AddToCartView

urlpatterns=[
    path("customers/",CustomerListView.as_view(),name="customer_list_view"),
    path("customers/<int:id>/",CustomerDetailView.as_view(),name="customer_detail_view"),
    path("inventory/",ProductListView.as_view(),name="product_list_view"),
    path("inventory/<int:id>/",ProductDetailView.as_view(),name="product_detail_view"),
    path("order/",OrderListView.as_view(),name="order_list_view"),
    path("order/<int:id>/",OrderDetailView.as_view(),name="order_detail_view"),
    path("cart/", CartListView.as_view(),name="cart_list_view"),
    path("cart/<int:id>/", CartDetailView.as_view(),name="cart_detail_view"),
    path("orders/", OrderListView.as_view(),name="order_list_view"),
    path("orders/<int:id>/", OrderDetailView.as_view(),name="order_detail_view"),
    path("add_to_cart/", AddToCartView.as_view(),name="add_to_cart_view"),
#     path("cart/",CartListView.as_view(),name="cart_list_view"),
#     path("cart/<int:id>/",CartDetailView.as_view(),name="cart_detail_view"),
#    path("cart/add_to_cart/<int:id>/", Add_To_CartView.as_view(), name="add_to_cart")
 
]