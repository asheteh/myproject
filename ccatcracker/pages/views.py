from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from .models import Center
from .models import Ranks



def index(request):
  
    return render(request,'pages/index.html')

def about(request):
    return render(request,'pages/about.html')


def ccat(request):
    #emails = ['abhijeets7661@gmail.com','abhijeets762@hmail.com']
    #context = {
    #    'news': 'We have good news!'
    #}
    #send_html_email(emails, 'Good news', 'email.html', context)  
    return render(request,'pages/ccat.html')

def cdac(request):
    return render(request,'pages/cdac.html')

def ccee(request):
    return render(request,'pages/ccee.html')

def test(request):
    return render(request,'pages/test.html')


def search(request):
    
    queryset_list =  Center.objects.all();

   
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact = city)
    
    #lte is less than eqyual to
    
    if 'course' in request.GET:
        course = request.GET['course']
        if course:
            queryset_list = queryset_list.filter(course__iexact = course)

    context = {
       
        'courses':queryset_list,
        'values' : request.GET
    }
    
    return render(request,'pages/search.html',context)


def rank(request):
    queryset_list =  Ranks.objects.all();

   
    if 'rank' in request.GET:
        rank = request.GET['rank']
        if rank:
            queryset_list = queryset_list.filter(rank__gte = rank)
    
    #lte is less than eqyual to
    
    if 'course' in request.GET:
        course = request.GET['course']
        if course:
            queryset_list = queryset_list.filter(course__iexact = course)

    context = {
       
        'courses':queryset_list,
        'values' : request.GET
    }
    
    return render(request,'pages/get_college.html',context)



# send html email
'''def send_html_email(to_list, subject, template_name, context, sender='thinkgeek.testing@gmail.com'):
    msg_html = render_to_string(template_name, context)
    msg = EmailMessage(subject=subject, body=msg_html, from_email=sender, bcc=to_list)
    msg.content_subtype = "html"  # Main content is now text/html
    msg.attach_file('notes/aws-udemy.pdf')
    return msg.send()
'''