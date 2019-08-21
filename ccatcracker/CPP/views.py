from django.shortcuts import render,redirect
from django.http import HttpResponse

def cpp(request):
    return render(request,'cpp/index.html')

def oops(request):
    return render(request,'cpp/oops.html')

def day2(request):
    return render(request,'cpp/functions.html')


def day3(request):
    return render(request,'cpp/class.html')

def day4(request):
    return render(request,'cpp/pointers.html')

def day4_a(request):
    return render(request,'cpp/array.html')