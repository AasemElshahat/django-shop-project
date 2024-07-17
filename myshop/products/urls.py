from django.urls import path
from . import views

urlpatterns = [
  path('bikes/', views.product_list, name='product_list'),
  path('bikes/<int:pk>/', views.product_detail, name='product_detail'),
  path('e-bikes/', views.ebike_list, name='ebike_list'),
  path('accessories/', views.accessory_list, name='accessory_list'),
  path('clothing/', views.clothing_list, name='clothing_list'),
  path('search/', views.search_products, name='search_products'),
]
