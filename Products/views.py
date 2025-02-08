from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password,check_password
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

# @login_required(login_url="/login/")
def HomePage(request):

    pro_objs = ProductDetail.objects.all()





    return render(request, "Index.html",{"pro_objs":pro_objs})

# @login_required(login_url="/login/")
def PizzaPage(request):
    pro_objs = ProductDetail.objects.filter(category__cat_name="Pizza")

    return render(request,"pizza.html",{"pro_objs":pro_objs})


# @login_required(login_url="/login/")
def BurgerPage(request):
    pro_objs = ProductDetail.objects.filter(category__cat_name="Burgers")

    return render(request,"burgers.html",{"pro_objs":pro_objs})



def LoginPage(request):
    message = ""

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
            
        try:
                # Attempt to find the customer by username
            customer = Customer.objects.get(username=username)
                
                # Check if the password matches
            if check_password(password, customer.password):
                    # Manually log the user in by creating a session
                request.session['customer_username'] = customer.username  
                # Store the customer ID in the session
                return redirect("/")  # Redirect to homepage or any other page after successful login
            else:
                message = "Incorrect password"
        except Customer.DoesNotExist:
                message = "Customer not found"
        
    return render(request, "login.html", {"message": message})



@login_required(login_url="/login/")
def LogoutPage(request):
    logout(request)
    return redirect("/")



def RegisterPage(request):
    message = ""
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        phone_number = request.POST["phone_number"]
        email = request.POST["email"]
        password = make_password(request.POST["password"])
        profile_image = request.FILES.get("profile_image")

        try:
            # Check if the username already exists
            customer = Customer.objects.get(username=username)
            message = "Please Choose a Different Username or Email, the current one is not available."
        except ObjectDoesNotExist:
            # Create the customer object
            customer = Customer.objects.create(
                first_name=first_name,
                last_name=last_name,
                phone=phone_number,
                email=email,
                password=password,
                profile_image=profile_image,
                username=username
            )
            # Log the user in immediately after successful registration
             # Log the user in
            message = "User Registration Successful and Logged In"
           

    return render(request, "Register.html", {"message": message})

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


