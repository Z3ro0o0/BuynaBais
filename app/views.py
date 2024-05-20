from rest_framework import status  # Add this import
from .models import Product, Category, Cart, Review, Ewallet
from .serializers import ProductSerializer, CategorySerializer, CartSerializer, CheckoutSerializer, OrderSerializer

from django.http import JsonResponse
from .serializers import CustomUserSerializer, ReviewSerializer, EwalletSerializer
from rest_framework.views import APIView
from .models import Cart, Checkout, Order, Ewallet, Product
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated



class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartListCreateView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class EwalletListCreateView(generics.ListCreateAPIView):
    queryset = Ewallet.objects.all()
    serializer_class = EwalletSerializer

class EwalletDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ewallet.objects.all()
    serializer_class = EwalletSerializer

class CheckoutListCreateView(generics.ListCreateAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

class CheckoutDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProductsByCategoryView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category_id=category_id)
    
class SellerOrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        current_seller = self.request.user
        return Order.objects.filter(cart__product__user=current_seller)
    
class UserProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_authenticated:
            return current_user.product_set.all()
        else:
            # Return an empty queryset if the user is not authenticated
            return Product.objects.none()
        
class UserProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        return Product.objects.filter(user=current_user)