
from django.urls import path
from .views import *


urlpatterns = [
    path("payment/",payment_success,name="payment"),
    path("checkout/",checkout,name="checkout"),
    path("card_info/",card_info,name="card_info"),
    path("process_order/",process_order,name="process_order"),
    path("shipped_orders/",shipped_orders,name="shipped_orders"),
    path("pending_orders/",pending_orders,name="pending_orders"),
    path("order_details/<int:pk>",order_details,name="order_details"),

    



   
    ]

