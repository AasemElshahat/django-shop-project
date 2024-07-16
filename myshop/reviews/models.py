from django.db import models
from django.conf import settings  # Import settings to get the custom user model
from django.contrib.auth.models import User
from myshop.products.models import Product

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Correct the user field reference
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True) # optional
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"

    class Meta:
        unique_together = ('product', 'user')