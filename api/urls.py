
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from app.views import (
    CategoryListCreateView, CategoryDetailView,
    ProductListCreateView, ProductDetailView,
    CartListCreateView, CartDetailView,
    ReviewListCreateView, ReviewDetailView,
    EwalletListCreateView, EwalletDetailView,
    CheckoutListCreateView, CheckoutDetailView,
    OrderListCreateView, OrderDetailView,
    ProductsByCategoryView, SellerOrderListView, UserProductListView)
from app import views
from django.conf.urls.static import static

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('carts/', CartListCreateView.as_view(), name='cart-list-create'),
    path('carts/<int:pk>/', CartDetailView.as_view(), name='cart-detail'),
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('ewallets/', EwalletListCreateView.as_view(), name='ewallet-list-create'),
    path('ewallets/<int:pk>/', EwalletDetailView.as_view(), name='ewallet-detail'),
    path('checkouts/', CheckoutListCreateView.as_view(), name='checkout-list-create'),
    path('checkouts/<int:pk>/', CheckoutDetailView.as_view(), name='checkout-detail'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),


    path('products/bycategory/<int:category_id>/', ProductsByCategoryView.as_view(), name='products-by-category'),
    path('seller/orders/', SellerOrderListView.as_view(), name='seller_orders'),
    path('user/products/', UserProductListView.as_view(), name='user-products'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
