# Generated by Django 5.0.6 on 2024-07-16 20:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_cart_alter_product_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(choices=[('Bike Parts', 'Bike Parts'), ('Road Bike', 'Road Bike'), ('Gravel Bike', 'Gravel Bike'), ('Mountain Bike', 'Mountain Bike'), ('E-Bike', 'E-Bike'), ('Accessory', 'Accessory'), ('Clothing', 'Clothing')], null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category'),
        ),
    ]
