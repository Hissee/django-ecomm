from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('products',allprod, name = 'products')
]