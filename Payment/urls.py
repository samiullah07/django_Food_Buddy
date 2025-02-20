
from django.urls import path
from .views import *


urlpatterns = [
    path("payment/",payment_success,name="payment"),
    path("checkout/",checkout,name="checkout"),
    path("card_info/",card_info,name="card_info"),
    path("process_order/",process_order,name="process_order"),

   
    ]

