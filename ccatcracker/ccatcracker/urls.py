
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from pages import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    #path('ads',views.ads,name='ads'),
    url(r'^ads\.txt',views.ads,name='ads'),
    path('about',views.about,name='about'),
    path('ccat',views.ccat,name='ccat'),
    path('interview',views.interview,name='interview'),
    path('questions',views.questions,name='questions'),
    path('ccat_questions',views.ccat_questions,name='ccat_questions'),
    path('notify',views.notify,name='notify'),
    path('ccat_notify',views.ccat_notify,name='ccat_notify'),
    path('cdac',views.cdac,name='cdac'),
    path('ccee',views.ccee,name='ccee'),
    path('test',views.test,name='test'),
    path('search',views.search,name='search'),
    path('rank',views.rank,name='rank'),
    path('payment/',include('payment.urls')),
    path('OnlineTest/',include('OnlineTest.urls')),
    path('accounts/',include('accounts.urls')),
     path('C/',include('C.urls')),
    path('admin/', admin.site.urls),
]
 
