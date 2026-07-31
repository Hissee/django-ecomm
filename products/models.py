from django.db import models

# Create your models here.
# model is like database table
class Category(models.Model):
    # fields of the database table
    name = models.CharField(max_length=100, unique=True)
    desciption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    original_price = models.DecimalField(max_digits=7,decimal_places=2)
    selling_price = models.DecimalField(max_digits=7,decimal_places=2)
    stock = models.IntegerField()
    # on_delete = models.CASCADE mean if the category is delete the products with deleted category is also deleted
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    trending = models.BooleanField(default=False)
    tag = models.SlugField()
    # image = models.URLField()
    image = models.FileField(upload_to='static/uploads')
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)


    def __str__(self):
        return f'Product: {self.name}'
    