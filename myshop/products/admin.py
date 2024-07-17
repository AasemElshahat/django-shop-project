# admin.py

from django.contrib import admin
from .models import Product, ProductImage, Category

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['image']

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ['name', 'price', 'stock', 'discount']
    search_fields = ('name', 'description')
    list_filter = ('category',)
    fields = ['name', 'description', 'price', 'pdf', 'discount', 'stock', 'category', 'featured']

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Category)
