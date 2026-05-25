from django.urls import path
from . import views

urlpatterns = [
    # Main Pages
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),

    # Cart System
    path('cart/', views.cart_view, name='cart_view'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('decrease/<int:item_id>/', views.decrease_cart_item, name='decrease_cart_item'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

    # Checkout & Orders
    path('checkout/', views.checkout, name='checkout'),
    path('order-success/', views.order_success, name='order_success'),
    path('my-orders/', views.my_orders, name='my_orders'),

    # Authentication & Profile
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('profile/', views.profile_view, name='profile_view'), # Profile View ഉണ്ടാക്കിയ ശേഷം ഇത് active ആക്കാം
]