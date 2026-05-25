from django.contrib import admin
from .models import Product, CartItem, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'date_added')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Models-ൽ ഉള്ള കൃത്യമായ ഫീൽഡ് പേരുകൾ ഇവിടെ നൽകുന്നു
    list_display = ('id', 'user', 'total_amount', 'status', 'order_date')
    list_filter = ('status', 'order_date')
    readonly_fields = ('order_date',)