from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .Cart import Cart
from Products.models import ProductDetail
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

def cart_summary(request):
    return render(request, "cart.html")

def cart_add(request):
    try:
        # Get the cart
        cart = Cart(request)
        
        if request.POST.get('action') == 'post':
            product_id = request.POST.get('product_id')
            # product_qty = request.POST.get('product_qty')

            # Validate quantity
            # if not product_qty or not product_qty.isdigit() or int(product_qty) <= 0:
            #     return JsonResponse({'error': 'Invalid quantity'}, status=400)

            # Lookup product in DB
            product = get_object_or_404(ProductDetail, id=product_id)
            # Save to cart
            cart.add(product=product)

            # Get updated cart quantity
            cart_quantity = len(cart)

            return JsonResponse({"food":product.product_name})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)