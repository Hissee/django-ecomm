from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages

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
    if request.method == 'POST':
        # ProductForm cha form fata aako
        productForm = ProductForm(request.POST,request.FILES)
        if productForm.is_valid :
            productForm.save()
            return redirect('all-products')
    context = {
        'productForm': ProductForm
    }
    return render(request, 'products/addproducts.html',context)

def deleteProduct(request, product_id):
    product = Product.objects.get(id = product_id)
    product.delete()
    return redirect('all-products')

def updateProduct(request, product_id):
    product = Product.objects.get(id = product_id)
    if request.method == 'POST':
        productForm = ProductForm(request.POST,request.FILES, instance=product)
        if productForm.is_valid() :
            productForm.save()
            return redirect('all-products')
    context = {
        # instace is to fill product detail in product form
        'productForm': ProductForm(instance=product)
    }
    return render(request, 'products/updateproduct.html', context)