
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.cpp,name='intro'),
    path('oops-in-c++',views.oops,name='oops-in-c++'),
    path('function-in-cpp',views.day2,name='function-in-cpp'),
    path('class-in-cpp',views.day3,name='class-in-cpp'),
    path('pointers-in-cpp',views.day4,name='pointers-in-cpp'),
    path('array-in-cpp',views.day4_a,name='array-in-cpp'),
    
    #path('payment_test',views.payment_test,name='payment_test'),
     
]