from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from OnlineTest import views
urlpatterns = [
    path('',views.onlinetest,name='onlinetest'),
    path('start',views.start,name='start'),
    path('payment_test',views.payment_test,name='payment_test'),
    path('result',views.result,name='result'),
    path('CDAC-CCAT-DEC-2019-Test1',views.test,name='CDAC-CCAT-DEC-2019-Test1'),
    path('CDAC-CCAT-DEC-2019-Test2',views.test2,name='CDAC-CCAT-DEC-2019-Test2'), 
    path('result2',views.result2,name='result2'), 
   
]