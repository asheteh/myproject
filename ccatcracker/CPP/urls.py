
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
    path('constructor-in-cpp',views.day5,name='constructor-in-cpp'),
    path('friend-function-in-cpp',views.day6,name='friend-function-in-cpp'),
    path('static-members-in-cpp',views.day6_a,name='static-members-in-cpp'),
    path('overloading-in-cpp',views.day7,name='overloading-in-cpp'),
    path('Inheritance-in-cpp',views.day8,name='Inheritance-in-cpp'),
    #path('payment_test',views.payment_test,name='payment_test'),
    path('constructor-In-inheritance-cpp',views.day9,name='constructor-In-inheritance-cpp'),
    path('virtual-class-in-cpp',views.day10,name='virtual-class-in-cpp'),
]