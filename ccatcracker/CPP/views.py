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

def day5(request):
    return render(request,'cpp/constructor.html')


def day6(request):
    return render(request,'cpp/friend.html')

def day6_a(request):
     return render(request,'cpp/static.html')

def day7(request):
    return render(request,'cpp/overloading.html')


def day8(request):
    return render(request,'cpp/inheritance.html')

def day9(request):
    return render(request,'cpp/inheritance-1.html')

def day10(request):
    return render(request,'cpp/virtual.html')


def assignment(request):
    return render(request,'cpp/assignment.html')