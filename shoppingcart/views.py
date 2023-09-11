from django.shortcuts import render,redirect,get_object_or_404

from .models import Product_Cart
from inventory.models import Product
from .forms import CartForm
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = CartForm(request.POST)
        if form.is_valid():
            cart_item = form.save(commit=False)
            cart_item.product_name = product.name
            cart_item.product_price = product.price
            cart_item.product_image = product.image
            cart_item.save()
            return redirect("cart")
    else:
        form = CartForm()
    return render(request, "cart/add_to_cart.html", {"form": form, "product": product})
def cart(request):
    cart_items = Product_Cart.objects.all()
    for cart_item in cart_items:
        cart_item.total_price = cart_item.product_price * cart_item.product_quantity
    return render(request, "cart/cart.html", {"cart_items": cart_items})
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Product_Cart, id=cart_item_id)
    if request.method == "POST":
        cart_item.delete()
        return redirect("cart")
    return render(request, "cart/remove_from_cart.html", {"cart_item": cart_item})


def view_cart(request):
    product_cart = Product_Cart.objects.all()
    total_cart_price = 0
    for item in product_cart:
        item.total_price = item.product_price * item.product_quantity
        total_cart_price += item.total_price
    return render(request,"cart/view_cart.html", {"product_cart": product_cart, "total_cart_price": total_cart_price})
def update_cart(request, id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item = Product_Cart.objects.get(id=id)
        if quantity > 0:
            cart_item.product_quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('view_cart')
def remove_item(request, id):
    cart_item = Product_Cart.objects.get(id=id)
    cart_item.delete()
    return redirect('view_cart')
def empty_cart(request):
    Product_Cart.objects.all().delete()
    return redirect("view_cart")


   

    
    

    









