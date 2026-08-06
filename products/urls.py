from django.urls import path
from .views import *

urlpatterns = [
    path("allproducts",allprod,name='all-products'),
    path("addproducts",addproduct,name='add-products'),
    path("delete-product/<int:product_id>/", deleteProduct),
    path("update-product/<int:product_id>/", updateProduct, name='update-product'),
]