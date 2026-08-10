from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Create your models here.

class WebInfo(models.Model):
    title = models.CharField(max_length=100)
    favicon = models.FileField(upload_to='static/uploads')
    logo = models.FileField(upload_to='static/uploads')
    bio = models.TextField(blank=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20,validators=[MinLengthValidator, MaxLengthValidator(14)])
    address = models.CharField(max_length=100)
    fb_link = models.URLField(blank=True)
    insta_link = models.URLField(blank=True)

    def __str__(self):
        return self.title