# Generated by Django 5.0.6 on 2024-06-13 18:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cart',
            field=models.ManyToManyField(blank=True, null=True, related_name='carted_products', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='wishlist',
            field=models.ManyToManyField(blank=True, null=True, related_name='wishlisted_products', to=settings.AUTH_USER_MODEL),
        ),
    ]