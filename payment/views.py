from django.shortcuts import render,redirect,get_object_or_404
from .forms import PaymentUploadForm
from .models import Payment

# from paymen.models import Product


def payment_upload_view(request):
    if request.method=="POST":
        form=PaymentUploadForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=PaymentUploadForm()
    return render(request,"payment/payment_upload.html",{"form":form})


def payment_list(request):
    payments=Payment.objects.all()
    return render(request,"payment/payment_list.html",{"payments":payments})

def payment_detail(request,id):
    payment=Payment.objects.get(id=id)
    return render(request,"payment/payment_detail.html",{"payment":payment})

def payment_update_view(request,id):
    payment=Payment.objects.get(id=id)
    if request.method=="POST":
        form=PaymentUploadForm(request.POST,instance= payment)
        if form.is_valid():
            form.save()
        return redirect("payment_detail_view",id= payment.id)
    else:
        form=PaymentUploadForm(instance= payment)
    return render(request,"payment/payment_update.html",{"form":form})

def delete_payment(request,id):
    payment= get_object_or_404(Payment, id=id)
    if request.method == 'POST':
        payment.delete()
        return redirect("payment_list_view")
    return render(request,'payment/delete_payment.html', {"payment":payment})
   
    








