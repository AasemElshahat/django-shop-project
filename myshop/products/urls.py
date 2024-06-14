from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.product_list, name='product_list'),
  path('<int:pk>/', views.product_detail, name='product_detail'),
]
