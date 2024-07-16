from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm
from myshop.products.models import Product
from django.db import IntegrityError

@login_required
def review_create_or_edit(request, product_id, review_id=None):
    product = get_object_or_404(Product, id=product_id)
    
    if review_id:
        review = get_object_or_404(Review, id=review_id, user=request.user)
    else:
        review = Review(product=product, user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Your review has been submitted successfully.')
            except IntegrityError:
                messages.error(request, 'You have already reviewed this product.')
            return redirect('product_detail', pk=product_id)
        else:
            messages.error(request, 'There was an error with your review.')
    else:
        form = ReviewForm(instance=review)

    return render(request, 'reviews/review_form.html', {'form': form, 'product': product, 'review': review})

@login_required
def review_delete(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    product_id = review.product.id
    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Your review has been deleted successfully.')
        return redirect('product_detail', pk=product_id)
    return render(request, 'reviews/review_confirm_delete.html', {'review': review})
