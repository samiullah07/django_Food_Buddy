from django.shortcuts import render,HttpResponse,redirect
from .shipping_forms import ShipppingForm,PaymentForm
from .models import ShippingAddress,Order,OrderItem
from django.contrib import messages
from cart.Cart import Cart
from Products.models import ProductDetail,Profile
import datetime

# Create your views here.

def shipped_orders(request):
     if request.user.is_authenticated and request.user.is_superuser:
          orders = Order.objects.filter(shipped=True)
          
          if request.POST:
               shipped_status = request.POST["shipped_status"]
               num = request.POST["num"]

               if shipped_status=='True':
                    order = Order.objects.filter(id=num)
                    now = datetime.datetime.now()

                    order.update(shipped=False,shipped_date=now)
                    return redirect('shipped_orders')
               else:
                    order = Order.objects.filter(id=num)
                    now = datetime.datetime.now()

                    order.update(shipped=True,shipped_date=now)
                    return redirect('shipped_orders')

          return render(request,"shipped_orders.html",{"orders":orders})
     else:
          messages.error(request,"Accessd Denied")
          return redirect("Home")
def pending_orders(request):
     if request.user.is_authenticated and request.user.is_superuser:
          orders = Order.objects.filter(shipped=False)
          
          if request.POST:
               shipped_status = request.POST["shipped_status"]
               num = request.POST["num"]

               if shipped_status=='True':
                    order = Order.objects.filter(id=num)
                    now = datetime.datetime.now()

                    order.update(shipped=False,shipped_date=now)
                    return redirect('pending_orders')
               else:
                    order = Order.objects.filter(id=num)
                    now = datetime.datetime.now()

                    order.update(shipped=True,shipped_date=now)
                    return redirect('pending_orders')
          

          return render(request,"pending_orders.html",{"orders":orders})
          
     else:
          messages.error(request,"Accessd Denied")
          return redirect("home")
     
def order_details(request,pk):
     if request.user.is_authenticated and request.user.is_superuser:
          #Gettig order
          order = Order.objects.get(id=pk)
          #Getting each other items
          order_items = OrderItem.objects.filter(order=pk)

          #changing shipping status
          if request.POST:
               shipped_status = request.POST["shipped_status"]


               if shipped_status=='True':
                    now = datetime.datetime.now()
                    order = Order.objects.filter(id=pk)

                    order.update(shipped=False,shipped_date=now)
                    return redirect('Home')
               else:
                    now = datetime.datetime.now()
                    order = Order.objects.filter(id=pk)


                    order.update(shipped=True,shipped_date=now)
                    return redirect('Home')





         

          return render(request,"order_details.html",{"order_items":order_items,"order":order})
     else:
          messages.error(request,"Accessd Denied")
          return redirect("Home")



     

def process_order(request):
    if request.POST:
        cart = Cart(request)
        total_price = 0
        total_quantities = 0
        products = cart.get_prods()
    


        for product in products:
            product_id = str(product.id)

            if product.is_deal:
                    product_price = float(product.deal_price)  # Ensure it's a float
                    quantity = cart.cart.get(product_id, {}).get('quantity', 0)
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

             #Order item work
             quantites = cart.get_quantities
             order_id = create_order.pk

             for product_item in products:
                order_item_product = product_item.id

                if product_item.is_deal:
                     price = product_item.deal_price
                else:
                     price = product_item.prduct_price

                for key,value in quantites().items():
                     if key == str(product_item.id):
                          #value

                          create_order_item = OrderItem(order_id=order_id,product_id = order_item_product,user=request.user,price=price,quantity=value['quantity'])
                          create_order_item.save()

     
             #deleting cart items
             for key in list(request.session.keys()):
                  if key == 'session_key':
                       del request.session[key]


             #Deleting database items of old cart

             current_user = Profile.objects.filter(user__id = request.user.id)

             current_user.update(old_cart='')




             messages.success(request,"Order has been placed")

             return redirect("Home")
        else:
            

             create_order = Order(full_name=full_name,shipping_address=shipping_address,amount_paid=total_price)
             create_order.save()

             
             #Order item work
             quantites = cart.get_quantities
             order_id = create_order.pk

             for product_item in products:
                order_item_product = product_item.id

                if product_item.is_deal:
                     price = product_item.deal_price
                else:
                     price = product_item.prduct_price

                for key,value in quantites().items():
                     if key == str(product_item.id):
                          #value

                          create_order_item = OrderItem(order_id=order_id,product_id = order_item_product,price=price,quantity=value)
                          create_order_item.save()


            
             for key in list(request.session.keys()):
                  if key == 'session_key':
                       del request.session[key]



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
                quantity = cart.cart.get(product_id, {}).get('quantity', 0)
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


