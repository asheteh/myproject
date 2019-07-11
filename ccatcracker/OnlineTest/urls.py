from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from OnlineTest import views
urlpatterns = [
    path('',views.test,name='test'),
    path('start',views.start,name='start'),
    path('payment_test',views.payment_test,name='payment_test'),
     
]
