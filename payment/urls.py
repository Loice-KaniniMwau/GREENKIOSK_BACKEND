from django.urls import path
from .views import payment_upload_view
from .views import payment_list
from .views import payment_detail
from .views import payment_update_view
from .views import delete_payment

urlpatterns=[
    path("payments/upload/",payment_upload_view,name="payment_upload_view"),
    path("payments/list/",payment_list,name="payment_list_view"),
    path("payments/detail/<int:id>",payment_detail,name="payment_detail_view"),
    path("payments/edit/<int:id>/",payment_update_view,name="payment_update_view"),
     path("payments/delete/<int:id>/",delete_payment,name="payment_delete_view"),

]