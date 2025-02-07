from django.conf import settings
from django.conf.urls.static import static


from django.urls import path
from .views import *


urlpatterns = [
    path('',HomePage,name="Home"),
    path('pizza/',PizzaPage,name="pizza"),
    path("burgers/",BurgerPage,name="burgers"),
    path('get-api/',getApi, name='get_api'),]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)