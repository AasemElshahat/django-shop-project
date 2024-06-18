from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
  name = models.CharField(max_length=100)

class Product(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField()
  price = models.FloatField()
  # image = models.ImageField(upload_to='products/')
  pdf = models.FileField(upload_to='products/pdfs/')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  wishlist = models.ManyToManyField(get_user_model(), null=True, blank=True,related_name='wishlisted_products')
  cart = models.ManyToManyField(get_user_model(), null=True, blank=True,related_name='carted_products')
  discount = models.IntegerField(default=0)
  stock = models.IntegerField(default=0)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return self.name
  

class ProductImage(models.Model):
  product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
  image = models.ImageField(upload_to='products/')
  
  def __str__(self):
    return f"{self.product.name} Image"