from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Cart
from products.models import Product


@login_required
def cart(request):
    user = request.user
    items = user.cart.items.all()
    return render(request, 'carts/cart.html', {'items': items})


@login_required
def add_to_cart(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    cart.items.add(product)
    cart.save()
    return redirect('cart')


@login_required
def remove_from_cart(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    cart.items.remove(product)
    cart.save()
    return redirect('cart')


@login_required
def remove_all_from_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart.items.clear()
    cart.save()
    return redirect('cart')
