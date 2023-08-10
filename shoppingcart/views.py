from django.shortcuts import render,redirect,get_object_or_404
from .forms import CartUploadForm
# from invento.models import Product
from shoppingcart.models import ShoppingCart
from inventory.models import Product
from .forms import AddToCartForm
# Create your views here.

def cart_upload_view(request):
    if request.method=="POST":
        form=CartUploadForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CartUploadForm()
    return render(request,"cart/cart_upload.html",{"form":form})


def cart_list(request):
    carts=ShoppingCart.objects.all()
    return render(request,"cart/cart_list.html",{"carts":carts})

def cart_detail(request,id):
    cart=ShoppingCart.objects.get(id=id)
    return render(request,"cart/cart_detail.html",{"cart":cart})

def cart_update_view(request,id):
    cart=ShoppingCart.objects.get(id=id)
    if request.method=="POST":
        form=CartUploadForm(request.POST,instance=cart)
        if form.is_valid():
            form.save()
        return redirect("cart_detail_view",id=cart.id)
    else:
        form=CartUploadForm(instance=cart)
    return render(request,"cart/edit_cart.html",{"form":form})


def add_to_cart(request,id):
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            user = request.user 
            product = get_object_or_404(Product, id=id)
            cart_item, created = ShoppingCart.objects.get_or_create(user=user, product=product)
            cart_item.quantity += quantity
            cart_item.save()
            return redirect('cart_list_view')  # Redirect to the cart list
    else:
        form = AddToCartForm()
    return render(request, 'add_to_cart.html', {'form': form,"id":id})
def cart_view(request):
    user = request.user
    cart_items = ShoppingCart.objects.filter(user=user)
    total_amount = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart_list.html', {'cart_items': cart_items, 'total_amount': total_amount})


   

    
    

    









