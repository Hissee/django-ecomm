from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
# def index(request):
#     # return HttpResponse("Hello World")
#     context = {
#         'products': Product.objects.all()
#     }
#     return render(request, 'index.html',context)
# def about(request):
#     return render(request, 'about.html')

def allprod(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'products/allproducts.html',context)

def addproduct(request):
    context = {
        'productForm': ProductForm
    }
    return render(request, 'products/addproducts.html',context)