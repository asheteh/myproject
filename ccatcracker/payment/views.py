from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib import messages, auth
from paytm import checksum
from . models import Orders
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
MERCHANT_KEY = 'kbzk1DSbJiV_O3p5'      

def checkout(request):
   
    return render(request,'payment/checkout.html')

def exam_checkout(request):
    return render(request,'payment/exam_checkout.html')

def payment(request):
        if request.method == 'POST':
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            state = request.POST.get('state', '')
            city = request.POST.get('city', '')
           
            phone = request.POST.get('phone', '')
            order = Orders(name=name, email=email,phone=phone,state=state,city=city)
            order.save()
        
            id = order.order_id
            param_dict = {
                'MID':'WorldP64425807474247',
                'ORDER_ID':str(order.order_id), 
                'TXN_AMOUNT':'200',
                'CUST_ID':order.email,
                'INDUSTRY_TYPE_ID':'Retail',
                'WEBSITE':'worldpressplg',
                'CHANNEL_ID':'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/payment/handlerequest',
            }
            param_dict['CHECKSUMHASH'] = checksum.generate_checksum(param_dict, MERCHANT_KEY)
            return render(request, 'payment/payment_form.html', {'param_dict': param_dict})
        return render(request, 'payment/checkout.html')
        

   


@csrf_exempt
def handlerequest(request):
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = True
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
            order = Orders.objects.get(order_id=response_dict['ORDERID'])
            order.status = "Placed"  # change field
            order.save()
            messages.success(request, 'Congrats Your Order Has Been Placed You Will Get Email Soon With Notes ...')
            # Send Mail
         
            send = [order.email]
            context = {
            'news': 'We have good news!'
            }
            send_html_email(send, 'Good news', 'email.html', context)
            order.status = "Sent" 
            order.save()  
        else:
            order.status = "Failed" 
            order.save() 
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'payment/paymentstatus.html', {'response': response_dict})



def send_html_email(to_list, subject, template_name, context, sender='thinkgeek.testing@gmail.com'):
    msg_html = render_to_string(template_name, context)
    msg = EmailMessage(subject=subject, body=msg_html, from_email=sender, bcc=to_list)
    msg.content_subtype = "html"  # Main content is now text/html
    msg.attach_file('notes/aws-udemy.pdf')
    return msg.send()

  
