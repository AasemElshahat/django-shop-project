from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from myshop.products.models import Product
from .models import CartItem, WishlistItem

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart:view_cart')

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    total_price = sum(item.get_total_price() for item in cart_items)
    context = {
        'cart_items': cart_items,
        'wishlist_items': wishlist_items,
        'total_price': total_price,
    }
    return render(request, 'cart/view_cart.html', context)

@login_required
def update_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        if quantity:
            cart_item.quantity = int(quantity)
            cart_item.save()
    return redirect('cart:view_cart')

@login_required
def remove_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.delete()
    return redirect('cart:view_cart')

@login_required
def empty_cart(request):
    CartItem.objects.filter(user=request.user).delete()
    return redirect('cart:view_cart')

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    WishlistItem.objects.get_or_create(user=request.user, product=product)
    return redirect('cart:view_wishlist')

@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    WishlistItem.objects.filter(user=request.user, product=product).delete()
    return redirect('cart:view_wishlist')

@login_required
def view_wishlist(request):
    cart_items = CartItem.objects.filter(user=request.user)
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    context = {
        'cart_items': cart_items,
        'wishlist_items': wishlist_items,
    }
    return render(request, 'cart/view_wishlist.html', context)
