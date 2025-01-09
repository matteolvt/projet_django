from django.contrib import admin

from home.models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','price')
    search_fields = ('title', 'category')
    list_filter = ('category','price')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)