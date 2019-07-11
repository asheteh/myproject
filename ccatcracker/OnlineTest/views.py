from django.shortcuts import render
from . models import OnlineTest
# Create your views here.
def test(request):
   o = OnlineTest.objects.all()
   context ={
        "page": o
    }
 
   return render(request,'OnlineTest/test.html')

def start(request):
   # o = OnlineTest.objects.all()
   # context ={
   #     "page": o
    #}
    return render(request,'OnlineTest/payment.html')


def payment_test(request):
   return render(request,'payment/exam_checkout.html')


       

