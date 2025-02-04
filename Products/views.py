from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from .models import *
# Create your views here.


def HomePage(request):
    page = "Home"

    pro_objs = ProductDetail.objects.all()





    return render(request, "Index.html",{"page":page,"pro_objs":pro_objs})




def getApi(request):
    pro_objs = ProductDetail.objects.all()

    product_name = request.GET.get("product-name")

    if product_name:
        pro_objs = pro_objs.filter(product_name__cat_name__icontains=product_name) 
    payload = []

    for pro_obj in pro_objs:
        payload.append({
            "Id" : pro_obj.id,
            "product-name" : pro_obj.product_name.cat_name,
            "product_des" : pro_obj.product_des,
            "product_price" : pro_obj.prduct_price,
            "product_image" : str(pro_obj.product_image)
        })


    return JsonResponse(payload,safe=False)


