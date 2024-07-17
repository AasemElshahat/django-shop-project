# from django.shortcuts import get_object_or_404, redirect, render
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse
# from .models import Review
# from .forms import ReviewForm
# from myshop.products.models import Product
# from django.db import IntegrityError
# from django.views.decorators.http import require_POST

# @login_required
# def review_create_or_edit(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     review = Review.objects.filter(product=product, user=request.user).first()

#     if request.method == 'POST':
#         form = ReviewForm(request.POST, instance=review)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.product = product
#             review.user = request.user
#             try:
#                 review.save()
#                 messages.success(request, 'Your review has been submitted successfully.')
#             except IntegrityError:
#                 messages.error(request, 'You have already reviewed this product.')
#             return redirect('product_detail', pk=product_id)
#     else:
#         form = ReviewForm(instance=review)

#     context = {
#         'form': form,
#         'product': product,
#         'review': review,
#     }
#     return render(request, 'reviews/review_form.html', context)

# @login_required
# @require_POST
# def review_delete(request, review_id):
#     review = get_object_or_404(Review, id=review_id, user=request.user)
#     product_id = review.product.id
#     review.delete()
#     messages.success(request, 'Your review has been deleted successfully.')
#     return redirect('product_detail', pk=product_id)

# @login_required
# def get_review_form(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     review = Review.objects.filter(product=product, user=request.user).first()
#     form = ReviewForm(instance=review)
    
#     context = {
#         'form': form,
#         'product': product,
#         'review': review,
#     }
#     return render(request, 'reviews/review_form.html', context)