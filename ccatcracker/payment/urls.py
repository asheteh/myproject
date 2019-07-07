from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from payment import views
urlpatterns = [
    path('',views.checkout,name='checkout'),
    path('payment',views.payment,name='payment'),
    path('handlerequest',views.handlerequest,name='handlerequest'),
   
]
