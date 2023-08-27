from django.urls import path
from .views import order_upload_view
from .views import order_list
from .views import order_update_view
from .views import delete_order
from .views import order_summary
urlpatterns=[
  path("order/upload/",order_upload_view,name="order_upload_view"),
  path("order/list/",order_list,name="order_list_view"),
  path("order/summary/",order_summary,name="order_summary_view"),
  path("order/update/<int:id>/",order_update_view,name="order_update_view"),
  path("order/delete/<int:id>/",delete_order,name="order_delete_view"),


]







