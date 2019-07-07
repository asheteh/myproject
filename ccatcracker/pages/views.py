from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

def index(request):
    return render(request,'pages/index.html')

def about(request):
    return render(request,'pages/about.html')


def ccat(request):
    #emails = ['abhijeets7661@gmail.com','abhijeets762@hmail.com']
    #context = {
    #    'news': 'We have good news!'
    #}
   # send_html_email(emails, 'Good news', 'email.html', context)  
    return render(request,'pages/ccat.html')

def cdac(request):
    return render(request,'pages/cdac.html')

def ccee(request):
    return render(request,'pages/ccee.html')

def test(request):
    return render(request,'pages/test.html')



def send_html_email(to_list, subject, template_name, context, sender='thinkgeek.testing@gmail.com'):
    msg_html = render_to_string(template_name, context)
    msg = EmailMessage(subject=subject, body=msg_html, from_email=sender, bcc=to_list)
    msg.content_subtype = "html"  # Main content is now text/html
    return msg.send()
