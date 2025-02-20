from django.shortcuts import render,HttpResponse,redirect
from .shipping_forms import ShipppingForm,PaymentForm
from .models import ShippingAddress,Order,OrderItem
from django.contrib import messages
from cart.Cart import Cart
from Products.models import ProductDetail

# Create your views here.



def process_order(request):
    if request.POST:
        cart = Cart(request)
        total_price = 0
        total_quantities = 0
        card_form = PaymentForm()
        products = cart.get_prods()
    


        for product in products:
            product_id = str(product.id)

            if product.is_deal:
                    product_price = float(product.deal_price)  # Ensure it's a float
                    quantity = cart.get(product_id, {}).get('quantity', 0)
                    product.total_price = product_price * quantity  # Calculate total price for each product
                    total_price += product.total_price  # Add to overall total price
                    total_quantities += quantity
            else:
                    product_price = float(product.prduct_price)  # Ensure it's a float
                    quantity = cart.cart.get(product_id, {}).get('quantity', 0)
                    product.total_price = product_price * quantity  # Calculate total price for each product
                    total_price += product.total_price  # Add to overall total price
                    total_quantities += quantity


        card_form = PaymentForm(request.POST or None)
        my_shipping = request.session.get('my_shipping')

        shipping_address = f"{my_shipping['address']}\n {my_shipping['city']}\n {my_shipping['zip_code']}\n{my_shipping['country']}"
        full_name = my_shipping["full_name"]
        email = my_shipping["email"]

        if request.user.is_authenticated:
             user = request.user

             create_order = Order(user=user,full_name=full_name,shipping_address=shipping_address,amount_paid=total_price)
             create_order.save()

             messages.success(request,"Order has been placed")

             return redirect("Home")

             
        



          
          
          
    else:
          messages.error(request,"Access denied")
          return redirect("Home")


def card_info(request):
    cart = Cart(request)
    total_price = 0
    total_quantities = 0
    card_form = PaymentForm()
    products = cart.get_prods()
    # adding shipping address in session
    my_shipping = request.POST
    request.session['my_shipping'] =my_shipping
    


    for product in products:
        product_id = str(product.id)

        if product.is_deal:
                product_price = float(product.deal_price)  # Ensure it's a float
                quantity = cart.get(product_id, {}).get('quantity', 0)
                product.total_price = product_price * quantity  # Calculate total price for each product
                total_price += product.total_price  # Add to overall total price
                total_quantities += quantity
        else:
                product_price = float(product.prduct_price)  # Ensure it's a float
                quantity = cart.cart.get(product_id, {}).get('quantity', 0)
                product.total_price = product_price * quantity  # Calculate total price for each product
                total_price += product.total_price  # Add to overall total price
                total_quantities += quantity

    if request.POST:
        return render(request,"card_info.html",{"total_price":total_price,"card_form":card_form})
    else:
        messages.error(request,"Access denined")
        return redirect("Home")



def checkout(request):
    
    if request.user.is_authenticated:
        shipping_user = ShippingAddress.objects.get(user__id = request.user.id)
        shipping_form = ShipppingForm(request.POST or None, instance=shipping_user)
  


        return render(request,"checkout.html",{"shipping_form":shipping_form})
    
    else:
        shipping_form = ShipppingForm(request.POST or None)

        return render(request,"checkout.html",{"shipping_form":shipping_form})


        

def payment_success(request):

    return render(request,"payment.html")


