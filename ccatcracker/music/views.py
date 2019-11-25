from django.shortcuts import render
from .models import Sargam

def music(request):
    
    return render(request,'music/main.html')

def song(request):
    return render(request,'music/bekhayali.html')


def song_list(request):
    try:
        if request.method == 'POST':
            song = request.POST.get('search', '')
           
            result = Sargam.objects.filter(song_name__iregex=r'['+song+']')
            text = Sargam.objects.filter(song_name__iexact =song)
           

            context={
                'songs' : text,
            }
           
        return render(request,'music/main.html',context)
    except:
        return render(request,'music/main.html')

def search(request):

     if request.method == 'POST':
            song = request.POST['search_text']
            
          
            text = Sargam.objects.filter(song_name__icontains=song)[:5]

           
     return render(request,'music/ajax_search.html',{'songs':text})

