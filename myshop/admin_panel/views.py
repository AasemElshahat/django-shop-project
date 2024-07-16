# admin_panel/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from myshop.products.models import Product, Category, ProductImage
from myshop.reviews.models import Review
from myshop.users.models import CustomUser
from myshop.reviews.forms import ReviewForm
from myshop.products.forms import ProductForm, ProductImageForm
from myshop.users.forms import UserForm

def is_admin(user):
    return user.is_superuser

def get_breadcrumbs(current_page):
    breadcrumbs = [
        {'name': 'Dashboard', 'url': '/admin-panel/'}
    ]
    if current_page != 'Dashboard':
        breadcrumbs.append({'name': current_page, 'url': ''})
    return breadcrumbs

@login_required
@user_passes_test(is_admin)
def dashboard(request):
    context = {
        'breadcrumbs': get_breadcrumbs('Dashboard'),
    }
    return render(request, 'admin_panel/dashboard.html', context)

# Product Views
@login_required
@user_passes_test(is_admin)
def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'breadcrumbs': get_breadcrumbs('Product List'),
    }
    return render(request, 'admin_panel/product_list.html', context)

@login_required
@user_passes_test(is_admin)
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully.')
            return redirect('admin_product_list')
    else:
        form = ProductForm()
    context = {
        'form': form,
        'breadcrumbs': get_breadcrumbs('Create Product'),
    }
    return render(request, 'admin_panel/product_form.html', context)

@login_required
@user_passes_test(is_admin)
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully.')
            return redirect('admin_product_list')
    else:
        form = ProductForm(instance=product)
    context = {
        'form': form,
        'breadcrumbs': get_breadcrumbs('Update Product'),
    }
    return render(request, 'admin_panel/product_form.html', context)

@login_required
@user_passes_test(is_admin)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully.')
        return redirect('admin_product_list')
    context = {
        'product': product,
        'breadcrumbs': get_breadcrumbs('Delete Product'),
    }
    return render(request, 'admin_panel/product_confirm_delete.html', context)

# Review Views
@login_required
@user_passes_test(is_admin)
def review_list(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
        'breadcrumbs': get_breadcrumbs('Review List'),
    }
    return render(request, 'admin_panel/review_list.html', context)

@login_required
@user_passes_test(is_admin)
def review_create_or_edit(request, pk=None):
    if pk:
        review = get_object_or_404(Review, pk=pk)
        page_title = 'Edit Review'
    else:
        review = Review()
        page_title = 'Create Review'
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review saved successfully.')
            return redirect('admin_review_list')
    else:
        form = ReviewForm(instance=review)
    context = {
        'form': form,
        'breadcrumbs': get_breadcrumbs(page_title),
    }
    return render(request, 'admin_panel/review_form.html', context)

@login_required
@user_passes_test(is_admin)
def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Review deleted successfully.')
        return redirect('admin_review_list')
    context = {
        'review': review,
        'breadcrumbs': get_breadcrumbs('Delete Review'),
    }
    return render(request, 'admin_panel/review_confirm_delete.html', context)

# User Views
@login_required
@user_passes_test(is_admin)
def user_list(request):
    users = CustomUser.objects.all()
    context = {
        'users': users,
        'breadcrumbs': get_breadcrumbs('User List'),
    }
    return render(request, 'admin_panel/user_list.html', context)

@login_required
@user_passes_test(is_admin)
def user_update(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully.')
            return redirect('admin_user_list')
    else:
        form = UserForm(instance=user)
    context = {
        'form': form,
        'breadcrumbs': get_breadcrumbs('Update User'),
    }
    return render(request, 'admin_panel/user_form.html', context)

@login_required
@user_passes_test(is_admin)
def user_delete(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully.')
        return redirect('admin_user_list')
    context = {
        'user': user,
        'breadcrumbs': get_breadcrumbs('Delete User'),
    }
    return render(request, 'admin_panel/user_confirm_delete.html', context)
