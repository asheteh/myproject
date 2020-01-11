from django.contrib.sitemaps.views import sitemap
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from pages import views
from .sitemap import StaticViewSitemap
sitemaps = {
    'static': StaticViewSitemap
}
urlpatterns = [
    url(r'^$',views.index,name='index'),
    #path('ads',views.ads,name='ads'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    url(r'^ads\.txt',views.ads,name='ads'),
    path('ccat-predac-course-pune',views.about,name='ccat-predac-course-pune'),
    path('cdac-c-cat',views.ccat,name='cdac-c-cat'),
    path('interview',views.interview,name='interview'),
    path('dac_interview',views.dac_interview,name='dac_interview'),
    path('big_data_interview',views.bd_interview,name='big_data_interview'),
    path('questions',views.questions,name='questions'),
    path('C-CAT-2019-Predac-Course',views.crashcourse,name='C-CAT-2019-Predac-Course'),
    path('ccat_questions',views.ccat_questions,name='ccat_questions'),
    path('notify',views.notify,name='notify'),
    path('ccat_notify',views.ccat_notify,name='ccat_notify'),
    path('cdac',views.cdac,name='cdac'),
    path('ccee',views.ccee,name='ccee'),
    path('previous',views.prev_questions,name='previous'),
    path('test',views.test,name='test'),
    path('search',views.search,name='search'),
    path('rank',views.rank,name='rank'),
    path('C-CPP-Programming-Questions',views.coding,name='C-CPP-Programming-Questions'),
    path('C-CPP-Objective-Questions',views.section_b,name='C-CPP-Objective-Questions'),
    path('English-Tutorial',views.eng,name='English-Tutorial'),
    path('Aptitude-Tutorial',views.apti,name='Aptitude-Tutorial'),
    path('Top-50-Interview-Questions-Data-Structure',views.data_structure_interview,name='Top-50-Interview-Questions-Data-Structure'),
    path('cpp-interview-question',views.cpp_interview,name='cpp-interview-question'),
    path('Top-50-Interview-Questions-Java',views.java_interview,name='Top-50-Interview-Questions-Java'),
    path('cdac-courses',views.other,name='cdac-courses'),
    path('dmc-cdac-course',views.dmc,name='dmc-cdac-course'),
    path('iot-cdac-course',views.iot,name='iot-cdac-course'),
    path('desd-cdac-course',views.desd,name='desd-cdac-course'),
    path('dittis-cdac-course',views.dittis,name='dittis-cdac-course'),
    path('hpcsa-cdac-course',views.hpcsa,name='hpcsa-cdac-course'),
    path('vlsi-cdac-course',views.vlsi,name='vlsi-cdac-course'),
    path('ai-cdac-course',views.ai,name='ai-cdac-course'),
    path('cdac-c-cat-syllabus',views.syllabus,name='cdac-c-cat-syllabus'),
    path('cdac-c-cat-result',views.result,name='cdac-c-cat-result'),
    path('cdac-c-cat-admit-card',views.admit,name='cdac-c-cat-admit-card'),




 
    path('payment/',include('payment.urls')),
    path('OnlineTest/',include('OnlineTest.urls')),
    path('accounts/',include('accounts.urls')),
    path('CPP/',include('CPP.urls')),
    path('music/',include('music.urls')),
    path('guitar/',include('guitar.urls')),
    path('C/',include('C.urls')),
    path('admin/', admin.site.urls),
]
 
