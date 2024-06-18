from django.shortcuts import render, get_object_or_404
from .models import Product, ProductImage, Category


# Search view
def home_view(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=query) | Product.objects.filter(description__icontains=query)
    return render(request, 'home.html', {'products': products, 'query': query})

def product_list_view(request):
    query = request.GET.get('q', '')
    products = Product.objects.all()
    
    if query:
        products = products.filter(name__icontains=query) | products.filter(description__icontains=query)
        no_results = not products.exists()
    else:
        no_results = False

    categories = Category.objects.all()
    selected_category = request.GET.get('category')
    if selected_category:
        products = products.filter(category__id=selected_category)
    
    context = {
        'products': products, 
        'categories': categories,
        'query': query,
        'no_results': no_results,
    }
    return render(request, 'product_list.html',context)



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

def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    product.discounted_price = get_discounted_price(product)
    product.stock_status = get_stock_status(product)
    context = {
        'product': product,
        'EMPTY_STOCK': EMPTY_STOCK,
        'LIMITED_STOCK_STATUS': LIMITED_STOCK_STATUS,
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