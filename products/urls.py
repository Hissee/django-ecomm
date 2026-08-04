from django.urls import path
from .views import *

urlpatterns = [
    path("allproducts",allprod,name='all=products'),
]