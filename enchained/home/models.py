from datetime import datetime
from xml.dom import ValidationErr
from django.db import models
from django import forms

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=90)
    # brandName = models.ForeignKey('Brand', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    content = models.TextField(null=True , blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Prodcuts'

    def str(self) -> str:
        return f"{self.title} - {self.category}"



class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'image', 'content', 'category', 'price']