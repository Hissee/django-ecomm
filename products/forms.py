from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        # model ra field key word ho
        # product model use garne vaneko
        model = Product
        # field k k halne
        fields = '__all__' #['name', 'selling_price', 'original price']