from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm
from myshop.products.models import Product
import logging
from django.db import IntegrityError

logger = logging.getLogger(__name__)

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
                reviews_html = render_to_string('reviews/review_list.html', {'product': product}, request=request)
                return JsonResponse({'success': True, 'reviews_html': reviews_html})
            except IntegrityError as e:
                logger.error(f"IntegrityError: {e}")
                return JsonResponse({'success': False, 'error': 'You have already reviewed this product.'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

    form = ReviewForm(instance=review)
    context = {'form': form, 'product': product}

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        form_html = render_to_string('reviews/review_form.html', context, request=request)
        return JsonResponse({'form': form_html})

    return render(request, 'reviews/review_form.html', context)


@login_required
def review_delete(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    product_id = review.product.id
    if request.method == 'POST':
        review.delete()
        return JsonResponse({'success': True, 'reload': True})

    return redirect('product_detail', pk=product_id)
