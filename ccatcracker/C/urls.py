from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('',views.intro,name='intro'),
    path('platform',views.platform,name='platform'),
    path('variables',views.variables,name='variables'),
    path('library',views.library,name='library'),
    path('data_types',views.data_types,name='data_types'),
    path('size_of',views.size_of,name='size_of'),
    path('modify_operator',views.modify,name='modify_operator'),
    path('control_statement',views.if_else,name='control_statement'),

    
    #path('payment_test',views.payment_test,name='payment_test'),
     
]
