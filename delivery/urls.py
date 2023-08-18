from django.urls import path
from .views import delivery_upload_view
from .views import delivery_detail
from .views import delete_delivery
from .views import delivery_list
from .views import delivery_update_view
urlpatterns=[
    path("shipment/upload/",delivery_upload_view,name="delivery_upload_view"),
    path("shipment/list/",delivery_list,name="delivery_list_view"),
    path("shipment/details/<int:id>",delivery_detail,name="delivery_detail_view"),
    path("shipment/edit/<int:id>",delivery_update_view,name="delivery_update_view"),
    path("shipment/delete/<int:id>/",delete_delivery,name="delete_delivery_view"),

]



    
    

    








