
# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from .forms import DeliveryUploadForm
from delivery.models import Delivery


def delivery_upload_view(request):
    if request.method=="POST":
        form=DeliveryUploadForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=DeliveryUploadForm()
    return render(request,"delivery/delivery_upload.html",{"form":form})


def delivery_list(request):
    delivery=Delivery.objects.all()
    return render(request,"delivery/delivery_list.html",{"delivery":delivery})

def delivery_detail(request,id):
    delivery=Delivery.objects.get(id=id)
    return render(request,"delivery/delivery_detail.html",{"product":delivery})

def delivery_update_view(request,id):
    delivery=Delivery.objects.get(id=id)
    if request.method=="POST":
        form=DeliveryUploadForm(request.POST,instance=delivery)
        if form.is_valid():
            form.save()
        return redirect("delivery_detail_view",id=delivery.id)
    else:
        form=DeliveryUploadForm(instance=delivery)
    return render(request,"delivery/delivery_edit.html",{"form":form})

def delete_delivery(request,id):
    delivery= get_object_or_404(Delivery,id=id)
    if request.method == 'POST':
        delivery.delete()
        return redirect("delivery_list_view")
    return render(request, "delivery/delete_delivery.html", {'delivery': delivery})
   

    








