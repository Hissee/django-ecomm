from django.contrib import admin
from .models import *

# Register your models here.

# For adding more properties to the listin admin pannel
class CategoryAdmin(admin.ModelAdmin):
    # to display in table
    list_display = ['name', 'id', 'created_at']
    # For search bar
    search_fields = ['name']

# need to register the Properties class
admin.site.register(Category, CategoryAdmin)

# for Products
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'selling_price', 'original_price','trending', 'stock', 'created_at']
    search_fields = ['name', 'description', 'category__name']
    list_filter = ['category','trending', 'created_at']
    list_editable = ['trending', 'stock', 'selling_price']

admin.site.register(Product, ProductAdmin)