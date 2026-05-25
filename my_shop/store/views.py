from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, CartItem, Order
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# 1. ഹോം പേജ് (Mall Hero & Scrolling Board)
def index(request):
    products = Product.objects.all()
    cart_items_count = 0
    if request.user.is_authenticated:
        cart_items_count = CartItem.objects.filter(user=request.user).count()
    return render(request, 'index.html', {
        'products': products,
        'cart_items_count': cart_items_count
    })

# 2. എബൗട്ട് പേജ് (Our Story)
def about(request):
    return render(request, 'about.html')

# 3. പ്രോഡക്റ്റ് ഡീറ്റെയിൽ പേജ്
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'detail.html', {'product': product})

# 4. കാർട്ട് വ്യൂ
@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

# 5. കാർട്ടിലേക്ക് ചേർക്കാൻ
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_view')

# 6. കാർട്ടിലെ എണ്ണം കുറയ്ക്കാൻ
@login_required
def decrease_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_view')

# 7. കാർട്ടിൽ നിന്ന് ഒഴിവാക്കാൻ
@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('cart_view')

# 8. ചെക്ക്ഔട്ട് & ഓർഡർ
def checkout(request):
    return render(request, 'checkout.html')

def order_success(request):
    return render(request, 'order_success.html')

def my_orders(request):
    return render(request, 'my_orders.html')

# 9. ലോഗിൻ സിസ്റ്റം (Auth)
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')