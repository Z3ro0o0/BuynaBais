from django.contrib.auth import get_user_model
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from .models import Category, Product, Cart, Review, Ewallet, Checkout, Order, MemberDetails


User = get_user_model()


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Review)
admin.site.register(Checkout)
admin.site.register(Order)
admin.site.register(Ewallet)
admin.site.register(MemberDetails)