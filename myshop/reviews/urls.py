from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:product_id>/review/', views.review_create_or_edit, name='review-create-or-edit'),
    path('product/<int:product_id>/review/<int:review_id>/', views.review_create_or_edit, name='review-create-or-edit'),
    path('review/<int:review_id>/delete/', views.review_delete, name='review-delete'),
]
