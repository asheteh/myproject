from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from accounts import views
urlpatterns = [
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('dashboard',views.dashboard,name='dashboard')
]
