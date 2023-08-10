from django.urls import path
# from .views import or_upload_view
# from .views import products_list
# from .views import product_detail
# from .views import product_update_view
# from .views import delete_product
from .views import customer_upload_view
from .views import customer_list
from .views import customer_update_view
from .views import customer_detail
from .views import delete_customer
urlpatterns=[
    path("user/upload/",customer_upload_view,name="customer_upload_view"),
    path("user/list/",customer_list,name="customer_list_view"),
    path("user/detail/<int:id>",customer_detail,name="customer_detail_view"),
    path("user/update/<int:id>",customer_update_view,name="customer_update_view"),
    path("user/delete/<int:id>",delete_customer,name="customer_delete_view"),
    #  path("products/delete/<int:id>",delete_product,name="product_delete"),

]

# from django.urls import path
# from .views import customer_upload_view
# from .views import customer_list
# from .views import customer_detail
# from .views import customer_update_view
# from .views import delete_customer

# urlpatterns[
#   path("customer/upload/",customer_upload_view,name="customer_upload_view"),
#   path("customer/list/",customer_list,name="customer_upload_view"),
#   path("customer/update/",customer_update_view,name="customer_upload_view"),
#     path("customer/detail/",customer_detail,name="customer_upload_view"),

# ]
 