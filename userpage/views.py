from django.shortcuts import render
from products.models import *
# Create your views here.

def index(request):
    context = {
        # 'products' : Product.objects.all()
        'trendingProducts' : Product.objects.filter(trending = True).order_by('-id')[:4]
        
    }
    return render(request, 'design/index.html',context)

def allprod(request):
    context = {
        'products': Product.objects.all()
        
    }
    return render(request, 'design/products.html',context)
