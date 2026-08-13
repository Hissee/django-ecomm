from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate, login, logout

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
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'] # json ma vako lai python usable ma convert garne
            password = form.cleaned_data['password'] 
            data = authenticate(username = username, password = password)

            if data is not None:
                login(request,data)
                messages.success(request, 'User has been Logged-in')
                return redirect('/')
            else :
                messages.error(request, 'Invalid username or password')
                return render(request, 'auth/login.html')
    context = {
        'loginForm' : LoginForm
    }
    return render(request, 'auth/login.html', context)

def userLogout(request):
    logout(request)
    messages.success(request, 'User has been Logged-out')
    return redirect('/')