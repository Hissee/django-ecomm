from django.shortcuts import render
from products.models import *

# Create your views here.

def index(request):
    context = {
        # 'products' : Product.objects.all()
        'products' : Product.objects.filter(trending = True).order_by('-id')[:4]
    }
    return render(request, 'design/index.html',context)