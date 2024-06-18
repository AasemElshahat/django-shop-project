from django.contrib import admin
from .models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Number of extra forms to display
    fields = ['image']

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ['name', 'price', 'stock', 'discount']  # Display these fields in the product list
    search_fields = ('name', 'description')
    list_filter = ('category',)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)