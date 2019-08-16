
from django.shortcuts import render,redirect
from django.http import HttpResponse

def intro(request):
    return render(request,'C/intro.html')

def platform(request):
    return render(request,'C/platform.html')

def variables(request):
    return render(request,'C/variables.html')

def functions(request):
    return HttpResponse("HHHH")

def library(request):
    return render(request,'C/library.html')

def data_types(request):
   
    return render(request,'C/data_types.html')


def size_of(request):
     return render(request,'C/size_of.html')

def modify(request):
     return render(request,'C/modify.html')

def if_else(request):
    return render(request,'C/if_else.html')

def loop(request):
    return HttpResponse("HHHH")

def exercise(request):
    return HttpResponse("HHHH")

def program(request):
    return HttpResponse("HHHH")

def recurssion(request):
    return HttpResponse("HHHH")


def array(request):
    return HttpResponse("HHHH")

def string(request):
    return HttpResponse("HHHH")

def structure(request):
    return HttpResponse("HHHH")

def union(request):
    return HttpResponse("HHHH")

def pointers(request):
    return HttpResponse("HHHH")

def memory_allocation(request):
    return HttpResponse("HHHH")

def some_extra(request):
    return HttpResponse("HHHH")


