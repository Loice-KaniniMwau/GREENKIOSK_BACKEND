from django.shortcuts import render,redirect,get_object_or_404
from .forms import OrderUploadForm
from order.models import Order
from shoppingcart.models import ShoppingCart
from inventory.models import Product

def order_upload_view(request):
    if request.method=="POST":
        form= OrderUploadForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=OrderUploadForm()
    return render(request,"order/order_upload.html",{"form":form})


def order_list(request):
    orders=Order.objects.all()
    return render(request,"order/order_list.html",{"orders":orders})

def order_summary(request):
    product_cart = ShoppingCart.objects.all()
    total_cart_price = 0
    for item in product_cart:
        item.total_price = item.product_price * item.product_quantity
        total_cart_price += item.total_price
    return render(request, "order/order_summary.html", {"product_cart": product_cart, "total_cart_price": total_cart_price})
def order_update_view(request,id):
    order=Order.objects.get(id=id)
    if request.method=="POST":
        form=OrderUploadForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
        return redirect("order_detail_view",id=order.id)
    else:
        form=OrderUploadForm(instance=order)
    return render(request,"order/order_edit.html",{"form":form})

def delete_order(request,id):
    order= get_object_or_404(Order, id=id)
    if request.method == 'POST':
        order.delete()
        return redirect("order_list_view")
    
    return render(request, 'order/order_delete.html', {'order': order})
    








    

    








