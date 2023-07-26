from django.contrib import admin
from .models import CustomUser, Category, Product, Cart, CartItem, Order, OrderItem, Review, Wishlist, WishlistItem, Shipping, Payment


# Register the models and their respective admin classes
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
admin.site.register(Wishlist)
admin.site.register(WishlistItem)
admin.site.register(Shipping)
admin.site.register(Payment)
admin.site.register(CustomUser)