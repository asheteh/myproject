from django.shortcuts import render,redirect
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.contrib import messages, auth
from .models import Test_1,Score,Test_2,Score2
from django.urls import resolve
  
# Create your views here.

def onlinetest(request):
      return render(request,'OnlineTest/ccat-test.html')
       
def test(request):
      if  request.user.is_authenticated:
          user = request.user
          try:
               p = Score.objects.get(username=user)
               p.mark = 0
               p.save()
               
          except:
            pass
            
      apti_question = Test_1.objects.filter(id__iexact=1)
        
        
      context = {
            
            
            'listings':apti_question
            
         }
      return render(request,'OnlineTest/test.html',context)
    

def start(request):
   # o = OnlineTest.objects.all()
   # context ={
   #     "page": o
    #}
    return render(request,'OnlineTest/payment.html')


def payment_test(request):
   return render(request,'payment/exam_checkout.html')


def result(request):
   print("1st call")
   
   if request.method == 'POST' and request.user.is_authenticated:
        user = request.user
        opt = request.POST.get('q', '')
        l = opt.split(" ")
        ans = l[0]
        qno = l[1]
        try:
         p = Score(username=user)
         p.save()
        except:
           pass
        print(opt)
        query=Test_1.objects.get(id=qno)
       
        real_ans = query.ans
        print(real_ans,ans)
        if ans == real_ans:
               usern=Score.objects.get(username=user)
               score =  usern.score
               print(score)
               p = Score.objects.get(username=user)
               p.score = score+1
               q = p.qno
               
               p.qno = q+1
               p.marks = score+1
               p.save()
               apti_question = Test_1.objects.filter(id__iexact = q+1)
               if apti_question:
                 
                  context = {
            
            
                  'listings':apti_question
            
                  }
                  return render(request,'OnlineTest/test.html',context)
               else:
                   usern=Score.objects.filter(username__iexact=user)
                   p = Score.objects.get(username=user)
                   p.score = 0
                   p.qno = 1
                  
                   p.save()
                   cont={
                      'listings':usern
                   }
                   return render(request,'OnlineTest/result.html',cont)
                      

        else:
           
            p = Score.objects.get(username=user)
            q = p.qno+1
            p.qno =q
            p.save()
            apti_question = Test_1.objects.filter(id__iexact = q)
            if apti_question:
              
               conte = {
         
         
               'listings':apti_question
         
               }
               return render(request,'OnlineTest/test.html',conte)
            else:
                   print("Else")
                   usern=Score.objects.filter(username__iexact=user)
                   p = Score.objects.get(username=user)
                   p.score = 0
                   p.qno = 1
                   
                   p.save()
                   cont={
                      'listings':usern
                   }
                   return render(request,'OnlineTest/result.html',cont)
            
                
   else:
         return render(request,'accounts/login.html')



def test2(request):
      if  request.user.is_authenticated:
          user = request.user
          try:
               p = Score2.objects.get(username=user)
               p.mark = 0
               p.save()
               
          except:
            pass
            
      apti_question = Test_2.objects.filter(id__iexact=1)
        
        
      context = {
            
            
            'listings':apti_question
            
         }
      return render(request,'OnlineTest/test2.html',context)

def result2(request):
   print("Called")
   
   if request.method == 'POST' and request.user.is_authenticated:
        user = request.user
        opt = request.POST.get('q', '')
        l = opt.split(" ")
        ans = l[0]
        qno = l[1]
        try:
         p = Score2(username=user)
         p.save()
        except:
           pass
        
        query=Test_2.objects.get(id=qno)
       
        real_ans = query.ans
        print(real_ans,ans)
        if ans == real_ans:
               usern=Score2.objects.get(username=user)
               score =  usern.score
               print(score)
               p = Score2.objects.get(username=user)
               p.score = score+1
               q = p.qno
               
               p.qno = q+1
               p.marks = score+1
               p.save()
               apti_question = Test_2.objects.filter(id__iexact = q+1)
               if apti_question:
                 
                  context = {
            
            
                  'listings':apti_question
            
                  }
                  return render(request,'OnlineTest/test2.html',context)
               else:
                   usern=Score2.objects.filter(username__iexact=user)
                   p = Score2.objects.get(username=user)
                   p.score = 0
                   p.qno = 1
                  
                   p.save()
                   cont={
                      'listings':usern
                   }
                   return render(request,'OnlineTest/result.html',cont)
                      

        else:
           
            p = Score2.objects.get(username=user)
            q = p.qno+1
            p.qno =q
            p.save()
            apti_question = Test_2.objects.filter(id__iexact = q)
            if apti_question:
              
               conte = {
         
         
               'listings':apti_question
         
               }
               return render(request,'OnlineTest/test2.html',conte)
            else:
                   print("Else")
                   usern=Score2.objects.filter(username__iexact=user)
                   p = Score2.objects.get(username=user)
                   p.score = 0
                   p.qno = 1
                   
                   p.save()
                   cont={
                      'listings':usern
                   }
                   return render(request,'OnlineTest/result.html',cont)
            
                
   else:
         return render(request,'accounts/login.html')
   
   
   

