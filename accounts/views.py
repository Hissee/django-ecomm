from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import *

# Create your views here.

def userRegister(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User created succesfully')
            return redirect('/')

    context = {
        'form' : UserCreationForm,
    }
    # return render(request, 'register', context)
    return render(request, 'auth/register.html', context)

def userLogin(request):
    context = {
        'loginForm' : LoginForm
    }
    return render(request, 'auth/login.html', context)