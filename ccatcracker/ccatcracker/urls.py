
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from pages import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    path('about',views.about,name='about'),
    path('ccat',views.ccat,name='ccat'),
    path('cdac',views.cdac,name='cdac'),
    path('ccee',views.ccee,name='ccee'),
    path('test',views.test,name='test'),
    path('search',views.search,name='search'),
    path('rank',views.rank,name='rank'),
    path('payment/',include('payment.urls')),
    path('OnlineTest/',include('OnlineTest.urls')),
    path('accounts/',include('accounts.urls')),
    path('admin/', admin.site.urls),
]
 
