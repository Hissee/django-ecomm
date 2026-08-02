from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    # return HttpResponse("Hello World")
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'index.html',context)
def about(request):
    return render(request, 'about.html')