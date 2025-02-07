from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from .models import *
# Create your views here.


def HomePage(request):

    pro_objs = ProductDetail.objects.all()





    return render(request, "Index.html",{"pro_objs":pro_objs})

def PizzaPage(request):
    pro_objs = ProductDetail.objects.filter(category__cat_name="Pizza")

    return render(request,"pizza.html",{"pro_objs":pro_objs})


def BurgerPage(request):
    pro_objs = ProductDetail.objects.filter(category__cat_name="Burgers")

    return render(request,"burgers.html",{"pro_objs":pro_objs})



def getApi(request):
    payload = []

    orders = Order.objects.all()

    for order in orders:
        payload.append({
            "Product Details" : order.productDetail.product_name,
            "Price" : order.productDetail.prduct_price,
            "Username" : order.customer.first_name,
            "Address" : order.address,
            "quantity" : order.quanitiy,
            "date" : order.date,
            "status" : order.status,
        })



    return JsonResponse(payload,safe=False)


