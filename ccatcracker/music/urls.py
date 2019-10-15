
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.music,name='music'),
    path('bekhayali-kabir-sing-2019-notation-sargam-tabs',views.song,name='bekhayali-kabir-sing-2019-notation-sargam-tabs'),
    path('song_list',views.song_list,name='song_list'),
    path('search_console',views.search,name='search_console'),
    
  
  
]