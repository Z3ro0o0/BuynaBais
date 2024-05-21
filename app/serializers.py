from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.conf import settings
from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.core.validators import RegexValidator
from rest_framework.settings import api_settings
from .models import Product, Category, Cart, Review, Checkout, Ewallet, Order

User = get_user_model()

class CustomUserCreateSerializer(UserCreateSerializer):
    confirm_password = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'birthdate', 'email', 'password', 'confirm_password']


    def validate(self, attrs):
        confirm_password = attrs.get('confirm_password')
        attrs.pop('confirm_password')
        user = User(**attrs)
        password = attrs.get("password")

        if confirm_password != password:
            raise serializers.ValidationError({'password': 'Passwords do not match'})

        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error[api_settings.NON_FIELD_ERRORS_KEY]}
            )

        return attrs

    def validate_password(self, value):
        regex_pattern = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+}{":;\'])(?=.*[a-zA-Z]).{8,}$'

        validator = RegexValidator(
            regex=regex_pattern,
            message="Password must contain at least 8 characters, one uppercase letter, one lowercase letter, one digit, and one special character.",
            code="invalid_password"
        )

        validator(value)

        return value
    
class CustomUserSerializer(UserSerializer):

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'birthdate'
        )
        read_only_fields = ('id', 'first_name', 'last_name', 'username', 'email' , 'birthdate')


class UserField(serializers.RelatedField) :
    def to_representation(self, value):
        return {
            'id': value.id,
            'first_name' : value.first_name,
            'last_name' : value.last_name,
        }

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'   

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "size": instance.size,
            "quantity": instance.quantity,
            "user": instance.user.id,
            "product": instance.product.id,
            "product_name" : instance.product.product_name,
            "price" : instance.product.price
        }

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'user' : {'id': instance.user.id, 'first_name': instance.user.first_name, 'last_name' : instance.user.last_name},
            'product' : {'id':instance.product.id },
            "review": instance.review,
            "variation": instance.variation,
            "productQuality": instance.productQuality,
            "performance": instance.performance,
            "bestFeatures": instance.bestFeatures
        }

class EwalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ewallet
        fields = '__all__'

# class CartField(serializers.RelatedField) :
#     def to_representation(self, value):
#         return {
#             'id': value.id,
#             'cart' : value.first_name,
#             'last_name' : value.last_name,
#         }
    
class OrderSerializer(serializers.ModelSerializer):
    cart = serializers.PrimaryKeyRelatedField(many=True, queryset=Cart.objects.all())
    class Meta:
        model = Order
        fields = '__all__'
    

class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = '__all__'



