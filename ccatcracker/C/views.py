
from django.shortcuts import render,redirect
from django.http import HttpResponse

def intro(request):
    return render(request,'C/intro.html')

def platform(request):
    return render(request,'C/platform.html')

def variables(request):
    return render(request,'C/variables.html')


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


def exercise(request):
    return HttpResponse("HHHH")

def program(request):
    return render(request,'C/program.html')


def projects(request):
    return render(request,'C/projects.html')


def array(request):
    return render(request,'C/array.html')

def string(request):
    return render(request,'C/string.html')

def structure(request):
   return render(request,'C/structure.html')

def pointers(request):
    return render(request,'C/pointers.html')

def memory_allocation(request):
    return render(request,'C/memory.html')
def typedef(request):
    return render(request,'C/typedef.html')

def some_extra(request):
    return render(request,'C/some_extra.html')

def files(request):
    return render(request,'C/file.html')

