from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Avg, Q



def product_list(request):
    products = Product.objects.all()
    for product in products:
        product.discounted_price = get_discounted_price(product)
        product.stock_status = get_stock_status(product)
    context = {
        'products': products,
        'EMPTY_STOCK': EMPTY_STOCK,
        'LIMITED_STOCK_STATUS': LIMITED_STOCK_STATUS,
    }  
    return render(request, 'products/product_list.html', context)


def average_rating(self):
    return self.reviews.aggregate(Avg('rating'))['rating__avg']

def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    user_review_exists = product.reviews.filter(user=request.user).exists()
    product.discounted_price = get_discounted_price(product)
    product.stock_status = get_stock_status(product)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]

    context = {
        'product': product,
        'EMPTY_STOCK': EMPTY_STOCK,
        'LIMITED_STOCK_STATUS': LIMITED_STOCK_STATUS,
        'user_review_exists': user_review_exists,
        'related_products': related_products,
    }
    return render(request, 'products/product_detail.html', context)

EMPTY_STOCK = "This product is not available at the moment"
LIMITED_STOCK_STATUS = "Limited products available"
IN_STOCK = "This product is available"

def get_discounted_price(product):
    if product.discount:
        return product.price * (1 - product.discount / 100)
    return product.price

def get_stock_status(product):
    if product.stock == 0:
        return EMPTY_STOCK
    elif product.stock < 5:
        return LIMITED_STOCK_STATUS
    else:
        return IN_STOCK

def ebike_list(request):
    category = get_object_or_404(Category, name='E-Bikes')
    ebikes = Product.objects.filter(category=category)
    for ebike in ebikes:
        ebike.discounted_price = get_discounted_price(ebike)
        ebike.stock_status = get_stock_status(ebike)
    context = {
        'products': ebikes,
        'category_name': 'E-Bikes',
        'EMPTY_STOCK': EMPTY_STOCK,
        'LIMITED_STOCK_STATUS': LIMITED_STOCK_STATUS,
    }
    return render(request, 'products/ebike_list.html', context)

def accessory_list(request):
    category = get_object_or_404(Category, name='Accessories')
    accessories = Product.objects.filter(category=category)
    for accessory in accessories:
        accessory.discounted_price = get_discounted_price(accessory)
        accessory.stock_status = get_stock_status(accessory)
    context = {
        'products': accessories,
        'category_name': 'Accessories',
        'EMPTY_STOCK': EMPTY_STOCK,
        'LIMITED_STOCK_STATUS': LIMITED_STOCK_STATUS,
    }
    return render(request, 'products/accessory_list.html', context)

def clothing_list(request):
    category = get_object_or_404(Category, name='Clothing')
    clothing = Product.objects.filter(category=category)
    for item in clothing:
        item.discounted_price = get_discounted_price(item)
        item.stock_status = get_stock_status(item)
    context = {
        'products': clothing,
        'category_name': 'Clothing',
        'EMPTY_STOCK': EMPTY_STOCK,
        'LIMITED_STOCK_STATUS': LIMITED_STOCK_STATUS,
    }
    return render(request, 'products/clothing_list.html', context)


# search view
def search_products(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(reviews__rating__icontains=query)
        ).distinct()
    else:
        products = Product.objects.all()

    for product in products:
        product.discounted_price = get_discounted_price(product)
        product.stock_status = get_stock_status(product)

    context = {
        'products': products,
        'query': query,
        'EMPTY_STOCK': EMPTY_STOCK,
        'LIMITED_STOCK_STATUS': LIMITED_STOCK_STATUS,
    }
    return render(request, 'products/search_results.html', context)