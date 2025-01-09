from django.db import models

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

    def __str__(self) -> str:
        return f"{self.title} - {self.category}"
    

class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)