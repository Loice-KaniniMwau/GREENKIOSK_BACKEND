from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect
from .models import Product_Cart
from datetime import datetime
from .models import Product
from order.models import Order
def view_cart(request):
    product_cart = Product_Cart.objects.all()
    total_cart_price = 0
    for item in product_cart:
        item.total_price = item.product_price * item.product_quantity
        total_cart_price += item.total_price
    return render(request, "cart/view_cart.html", {"product_cart": product_cart, "total_cart_price": total_cart_price})
def update_cart(request, id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item =Product_Cart.objects.get(id=id)
        if quantity > 0:
            cart_item.quantity = quantity
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
def add_to_cart(request, id):
    product = Product.objects.get(id=id)
    cart_item =Product_Cart(
        product_name = product.name,
        product_price = product.price,
        product_image = product.image,
        product_quantity = 1,
        date_added=datetime.now(),

        #   products= models.ManyToManyField(Product)
   
    )
    cart_item.save()
    return redirect("products_list_view")
def checkout_view(request, cart_id):
        try:
            cart = Product_Cart.objects.get(id=cart_id)
        except Product_Cart.DoesNotExist:
            return redirect('cart_not_found')
        if request.method == 'POST':
            order = Order.objects.create(
            user=cart.user,
            total_price=cart.get_total(),
        )
            order.products.set(cart.products.all())
            cart.products.clear()
            cart.save()
            return redirect('order_confirmation')
        return render(request, 'checkout.html', {'cart': cart})
def remove_product_from_cart(request, cart_id, product_id):
    cart = get_object_or_404(Product_Cart, id=cart_id)
    product = get_object_or_404(Product, id=product_id)
    if product in cart.products.all():
        cart.products.remove(product)
        cart.save()
    return redirect('view_cart')







