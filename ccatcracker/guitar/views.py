from django.shortcuts import render
from .models import chord
from .models import email_subscriptions

def chord_list(request):
    try:
    
        if request.method == 'POST':
            song = request.POST.get('query', '')
           
			
            text =  chord.objects.filter(song_names__icontains=song)[:10]
           

            context={
                'songs' : text,
            }
           
           
        return render(request,'guitar/guitar.html',context)
    except:
         return render(request,'guitar/guitar.html')

   
		


		   



def search(request):

     if request.method == 'POST':
            song = request.POST['search_text']
            
          
            text =  chord.objects.filter(song_names__icontains=song)[:5]

            
           
     return render(request,'guitar/ajax_search.html',{'songs':text})

def guitar(request):
    text =  chord.objects.filter(song_names__icontains='love')[:5]
    return render(request,'guitar/guitar.html',{"songs":text})



def Chaar_Kadam_Guitar_Tabs___Lead___PK_2014____Abhijeet(request):
	text = chord.objects.filter(id__iexact =2)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Aaj_Phir_Tumpe_Pyar_Aaya_Hai_Guitar_Tabs___Lead___Hate_Story_2___Abhijeet(request):
	text = chord.objects.filter(id__iexact =3)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tu_Chahiye_Guitar_Tabs___Lead___Bajrangi_Bhaijaan___Abhijeet(request):
	text = chord.objects.filter(id__iexact =4)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kya_Mujhe_Pyar_Hai_Guitar_Tabs___Lead___Woh_Lamhe___Abhijeet(request):
	text = chord.objects.filter(id__iexact =5)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def BAARISH_Guitar_Tabs___Lead___Yaariyan___Abhijeet(request):
	text = chord.objects.filter(id__iexact =6)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Dil_Aaj_Kal_Guitar_Tabs___Lead___Purani_Jeans___Abhijeet(request):
	text = chord.objects.filter(id__iexact =7)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def HUMDARD_Guitar_Tabs___Lead___Ek_Villain___Abhijeet(request):
	text = chord.objects.filter(id__iexact =8)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Hum_Mar_Jayenge__Aashiqui_2__Guitar_Tabs___Abhijeet(request):
	text = chord.objects.filter(id__iexact =9)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Saanson_Ko_Jeene_Ka_Guitar_Tabs___Lead___Zid__2014____Abhijeet(request):
	text = chord.objects.filter(id__iexact =10)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Share_a_link_on_Twitter(request):
	text = chord.objects.filter(id__iexact =11)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Teri_Meri_Teri_Meri_Guitar_Tabs___Lead___Bodygaurd___Abhijeet(request):
	text = chord.objects.filter(id__iexact =12)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Lag_Ja_Gale_Guitar_Tabs___Lead___Woh_Kaun_Thi___Abhijeet(request):
	text = chord.objects.filter(id__iexact =13)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Muskurane_Ki_Wajah_Tum_Ho_Guitar_Tabs___Lead___City_Lights___Abhijeet(request):
	text = chord.objects.filter(id__iexact =14)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Bin_Tere__Reprise__Guitar_Tabs___Lead___I_Hate_Love_Stories___Abhijeet(request):
	text = chord.objects.filter(id__iexact =15)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Iktara_Guitar_Tabs___Lead___Wake_Up_Sid___Abhijeet(request):
	text = chord.objects.filter(id__iexact =16)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Luka_Chuppi_Bahut_Huyi_Guitar_Tabs___Lead___Rang_De_Basanti___Abhijeet(request):
	text = chord.objects.filter(id__iexact =17)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Muskurane_Ki_Wajah_Tum_Ho_Guitar_Tabs___Lead___City_Lights___Abhijeet(request):
	text = chord.objects.filter(id__iexact =18)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Iktara_Guitar_Tabs___Lead___Wake_Up_Sid___Abhijeet(request):
	text = chord.objects.filter(id__iexact =19)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Aaj_Dil_Shayrana_Guitar_Tabs___Lead___Holiday___Abhijeet(request):
	text = chord.objects.filter(id__iexact =20)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Galliyan_Teri_Galiyan_Guitar_Tabs___Lead___Ek_Villain___Abhijeet(request):
	text = chord.objects.filter(id__iexact =21)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Main_Rang_Sharbaton_Ka__Phata_Poster_Nikla_Hero__Guitar_Tabs___Abhijeet(request):
	text = chord.objects.filter(id__iexact =22)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Humnava_Guitar_Tabs___Lead___Humari_Adhuri_Kahani___Abhijeet(request):
	text = chord.objects.filter(id__iexact =23)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Rehnuma_Guitar_Tabs___Lead___ROCKY_HANDSOME___Abhijeet(request):
	text = chord.objects.filter(id__iexact =24)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tere_Naam_Hamne_kiya_hai_Guitar_Tabs___Lead___Abhijeet(request):
	text = chord.objects.filter(id__iexact =25)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sun_Raha_Hai_na_tu__Aashiqui_2__Guitar_Tabs___Abhijeet(request):
	text = chord.objects.filter(id__iexact =26)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kaise_Mujhe_Tum_Mil_Gayi_Guitar_Tabs___Lead___Ghajini___Abhijeet(request):
	text = chord.objects.filter(id__iexact =27)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Mere_Mehboob_Qayamat_Hogi_Guitar_Tabs___Lead___Mr_X_In_Bombay___Abhijeet(request):
	text = chord.objects.filter(id__iexact =28)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Aashiyan_Guitar_tabs__Barfi____Abhijeet(request):
	text = chord.objects.filter(id__iexact =29)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tu_Hi_Tu_Har_Jagah_Guitar_Tabs___Lead___KICK__2014____Abhijeet(request):
	text = chord.objects.filter(id__iexact =30)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ek_Ladki_Ko_Dekha_To_Aisa_Laga_Guitar_Tabs___Lead___1942_Love_Story___Abhijeet(request):
	text = chord.objects.filter(id__iexact =31)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tera_Hone_Laga_Hoon_Guitar_Tabs___Lead___Ajab_Prem_Ki_Ghazab_Kahani___Abhijeet(request):
	text = chord.objects.filter(id__iexact =32)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Humko_Humise_Chura_Lo_Guitar_Tabs___Lead___Mohabbatein_Tune___Abhijeet(request):
	text = chord.objects.filter(id__iexact =33)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Neele_Neele_Ambar_Par_Guitar_Tabs___Lead___Kalakaar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =34)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Dheere_Dheere_Se_Guitar_Tabs___Lead___Aashiqui__1990____Abhijeet(request):
	text = chord.objects.filter(id__iexact =35)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def PANI_DA_RANG_vekh_ke_Guitar_Tabs___Lead___Vicky_Donor___Abhijeet(request):
	text = chord.objects.filter(id__iexact =36)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Re_Kabira_maan_jaa_Guitar_Tabs___Lead__Yeh_Jawaani_Hai_Deewani____Abhijeet(request):
	text = chord.objects.filter(id__iexact =37)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tum_Paas_Aaye_Guitar_Tabs___Lead___Abhijeet(request):
	text = chord.objects.filter(id__iexact =38)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Agar_Tum_Saath_Ho_Guitar_Tabs___Lead___Tamasha___Abhijeet(request):
	text = chord.objects.filter(id__iexact =39)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Pehla_Nasha_Pehla_Hummar_Guitar_Tabs___Lead___Jo_Jeeta_Wohi_Sikandar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =40)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tera_Chehra_Guitar_Tabs___Lead___SANAM_TERI_KASAM___ARIJIT_SINGH___Abhijeet(request):
	text = chord.objects.filter(id__iexact =41)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Chura_Liya_Hai_Tumne_Jo_Dil_Ko_Guitar_Tabs___Lead___Yaadon_Ki_Baarat___Abhijeet(request):
	text = chord.objects.filter(id__iexact =42)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Baatein_Ye_Kabhi_Na_Guitar_Tabs___Lead___Khamoshiyan___Abhijeet(request):
	text = chord.objects.filter(id__iexact =43)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kal_Ho_Naa_Ho_Guitar_Tabs___Lead___Title_Track___Abhijeet(request):
	text = chord.objects.filter(id__iexact =44)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Pehli_Pehli_Baar_Mohabbat_Ki_Hai_Guitar_Tabs___Lead___Sirf_Tum___Abhijeet(request):
	text = chord.objects.filter(id__iexact =45)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def O_O_Jaane_Jaana_Guitar_Tabs___Lead___Pyar_Kiya_To_Darna_Kya___Abhijeet(request):
	text = chord.objects.filter(id__iexact =46)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ek_Haseena_Thi_Ek_Deewana_Tha_Guitar_Tabs___Lead___Abhijeet(request):
	text = chord.objects.filter(id__iexact =47)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Gulabi_Aankhein_Jo_Teri_Dekhi_Guitar_Tabs___Lead___The_Train___Abhijeet(request):
	text = chord.objects.filter(id__iexact =48)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Hua_Hai_Aaj_Pehli_Baar_Guitar_Tabs___Lead___Sanam_Re___Abhijeet(request):
	text = chord.objects.filter(id__iexact =49)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Raabta_Guitar_Tabs___Lead___Agent_Vinod___Abhijeet(request):
	text = chord.objects.filter(id__iexact =50)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Bolna_Guitar_Tabs___Lead____Kapoor_and_Sons__Arijit_Singh___Abhijeet(request):
	text = chord.objects.filter(id__iexact =51)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Gerua_Guitar_Tabs___lead___Dilwale__2015____Abhijeet(request):
	text = chord.objects.filter(id__iexact =52)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Main_Rahoon_Ya_Na_Rahoon_Guitar_Tabs___Lead___Armaan_Malik___Abhijeet(request):
	text = chord.objects.filter(id__iexact =53)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Main_Hoon_Hero_Tera_Guitar_Tabs___Lead___Hero__Salman_Khan____Abhijeet(request):
	text = chord.objects.filter(id__iexact =54)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Chahun_Main_Ya_Na__Aashiqui_2__Guitar_Tabs___Abhijeet(request):
	text = chord.objects.filter(id__iexact =55)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def JEENA_JEENA_Guitar_Tabs___Lead___Badlapur__Atif_Aslam____Abhijeet(request):
	text = chord.objects.filter(id__iexact =56)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tujhe_Dekha_To_Ye_Jaana_Sanam_Guitar_Tabs___Lead___DDLJ_Tune___Abhijeet(request):
	text = chord.objects.filter(id__iexact =57)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kabhi_Jo_Baadal_Barse_Guitar_Tabs___Lead__Jackpot____Abhijeet(request):
	text = chord.objects.filter(id__iexact =58)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Main_Tenu_Samjhawan_Ki_Guitar_Tabs___Lead___Humpty_Sharma_Ki_Dulhania___Abhijeet(request):
	text = chord.objects.filter(id__iexact =59)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sanam_Re_Guitar_Tabs___Lead___Sanam_Re__Arijit_Singh____Abhijeet(request):
	text = chord.objects.filter(id__iexact =60)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ishq_Wala_Love_Guitar_Tabs___Lead___Student_of_the_Year__SOTY____Abhijeet(request):
	text = chord.objects.filter(id__iexact =61)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tum_hi_ho__Ashiqui_2__Guitar_Tabs___Abhijeet(request):
	text = chord.objects.filter(id__iexact =62)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Soch_Na_Sake_Guitar_Tabs___Lead___Airlift__Arijit_Singh____Abhijeet(request):
	text = chord.objects.filter(id__iexact =63)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Janam_Janam_Guitar_Tabs___Lead___Dilwale__2015____Abhijeet(request):
	text = chord.objects.filter(id__iexact =64)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def List_of_Best_Bollywood_Guitar_Songs_of_all_the_time___Best_Hindi_Songs__2015____Abhijeet(request):
	text = chord.objects.filter(id__iexact =65)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Main_Hoon_Hero_Tera_Guitar_Tabs___Lead___Hero__Salman_Khan____Abhijeet(request):
	text = chord.objects.filter(id__iexact =66)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Main_Rahoon_Ya_Na_Rahoon_Guitar_Tabs___Lead___Armaan_Malik___Abhijeet(request):
	text = chord.objects.filter(id__iexact =67)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tumhe_Apna_Banane_Ka_Guitar_Tabs___Lead___Hate_Story_3___Abhijeet(request):
	text = chord.objects.filter(id__iexact =68)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Agar_Tum_Saath_Ho_Guitar_Tabs___Lead___Tamasha___Abhijeet(request):
	text = chord.objects.filter(id__iexact =69)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Gerua_Guitar_Tabs___lead___Dilwale__2015____Abhijeet(request):
	text = chord.objects.filter(id__iexact =70)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Janam_Janam_Guitar_Tabs___Lead___Dilwale__2015____Abhijeet(request):
	text = chord.objects.filter(id__iexact =71)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sanam_Re_Guitar_Tabs___Lead___Sanam_Re__Arijit_Singh____Abhijeet(request):
	text = chord.objects.filter(id__iexact =72)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Soch_Na_Sake_Guitar_Tabs___Lead___Airlift__Arijit_Singh____Abhijeet(request):
	text = chord.objects.filter(id__iexact =73)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Hua_Hai_Aaj_Pehli_Baar_Guitar_Tabs___Lead___Sanam_Re___Abhijeet(request):
	text = chord.objects.filter(id__iexact =74)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kabhi_Jo_Baadal_Barse_Guitar_Tabs___Lead__Jackpot____Abhijeet(request):
	text = chord.objects.filter(id__iexact =75)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Meri_Maa_Mumma_Guitar_Tabs___Lead___Kailash_Kher__Dasvidaniya____Abhijeet(request):
	text = chord.objects.filter(id__iexact =76)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Saathiya_Pagle_Se_Dil_Ne_Ye_Kya_Kiya_Guitar_Tabs___Lead___Singham___Abhijeet(request):
	text = chord.objects.filter(id__iexact =77)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Chhoti_Si_Pyari_Si_Nanhi_Si_Guitar_Tabs___Lead___Anari___Abhijeet(request):
	text = chord.objects.filter(id__iexact =78)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Aashiyan_Guitar_tabs__Barfi____Abhijeet(request):
	text = chord.objects.filter(id__iexact =79)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Phoolon_Sa_Chehra_Tera_Guitar_Tabs___Lead___Anari___Abhijeet(request):
	text = chord.objects.filter(id__iexact =80)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tum_hi_ho__Ashiqui_2__Guitar_Tabs___Abhijeet(request):
	text = chord.objects.filter(id__iexact =81)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Main_Rang_Sharbaton_Ka__Phata_Poster_Nikla_Hero__Guitar_Tabs___Abhijeet(request):
	text = chord.objects.filter(id__iexact =82)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sun_Raha_Hai_na_tu__Aashiqui_2__Guitar_Tabs___Abhijeet(request):
	text = chord.objects.filter(id__iexact =83)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Chahun_Main_Ya_Na__Aashiqui_2__Guitar_Tabs___Abhijeet(request):
	text = chord.objects.filter(id__iexact =84)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Aashiqui_2_love_theme_Guitar_Tabs___Lead___Abhijeet(request):
	text = chord.objects.filter(id__iexact =85)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Hum_Mar_Jayenge__Aashiqui_2__Guitar_Tabs___Abhijeet(request):
	text = chord.objects.filter(id__iexact =86)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Arijit_Singh_Guitar_Tabs___Lead___Best_of_Arijit_Singh___Abhijeet(request):
	text = chord.objects.filter(id__iexact =87)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ashiqui_2_Movie_Guitar_Tabs___Lead___All_Songs_of_Ashiqui_2___Abhijeet(request):
	text = chord.objects.filter(id__iexact =88)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Re_Kabira_maan_jaa_Guitar_Tabs___Lead__Yeh_Jawaani_Hai_Deewani____Abhijeet(request):
	text = chord.objects.filter(id__iexact =89)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tujhe_Dekha_To_Ye_Jaana_Sanam_Guitar_Tabs___Lead___DDLJ_Tune___Abhijeet(request):
	text = chord.objects.filter(id__iexact =90)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def O_O_Jaane_Jaana_Guitar_Tabs___Lead___Pyar_Kiya_To_Darna_Kya___Abhijeet(request):
	text = chord.objects.filter(id__iexact =91)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Gulabi_Aankhein_Jo_Teri_Dekhi_Guitar_Tabs___Lead___The_Train___Abhijeet(request):
	text = chord.objects.filter(id__iexact =92)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Iktara_Guitar_Tabs___Lead___Wake_Up_Sid___Abhijeet(request):
	text = chord.objects.filter(id__iexact =93)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tum_Paas_Aaye_Guitar_Tabs___Lead___Abhijeet(request):
	text = chord.objects.filter(id__iexact =94)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tere_Naam_Hamne_kiya_hai_Guitar_Tabs___Lead___Abhijeet(request):
	text = chord.objects.filter(id__iexact =95)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def BAARISH_Guitar_Tabs___Lead___Yaariyan___Abhijeet(request):
	text = chord.objects.filter(id__iexact =96)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ek_Haseena_Thi_Ek_Deewana_Tha_Guitar_Tabs___Lead___Abhijeet(request):
	text = chord.objects.filter(id__iexact =97)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def PANI_DA_RANG_vekh_ke_Guitar_Tabs___Lead___Vicky_Donor___Abhijeet(request):
	text = chord.objects.filter(id__iexact =98)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Pehla_Nasha_Pehla_Hummar_Guitar_Tabs___Lead___Jo_Jeeta_Wohi_Sikandar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =99)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tere_Naina_Maar_Hi_Daalenge_Guitar_tabs___Jai_Ho___Abhijeet(request):
	text = chord.objects.filter(id__iexact =100)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Dil_Aaj_Kal_Guitar_Tabs___Lead___Purani_Jeans___Abhijeet(request):
	text = chord.objects.filter(id__iexact =101)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kyon_na_hum_tum_Guitar_Tabs__Barfi____Abhijeet(request):
	text = chord.objects.filter(id__iexact =102)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Mere_Mehboob_Qayamat_Hogi_Guitar_Tabs___Lead___Mr_X_In_Bombay___Abhijeet(request):
	text = chord.objects.filter(id__iexact =103)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Raabta_Guitar_Tabs___Lead___Agent_Vinod___Abhijeet(request):
	text = chord.objects.filter(id__iexact =104)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Galliyan_Teri_Galiyan_Guitar_Tabs___Lead___Ek_Villain___Abhijeet(request):
	text = chord.objects.filter(id__iexact =105)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def TU_HI_HAI_AASHIQUI_Guitar_Tabs___Dishkiyaoon___Abhijeet(request):
	text = chord.objects.filter(id__iexact =106)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Khali_Salam_Dua_Guitar_Tabs___Shortcut_Romeo___Abhijeet(request):
	text = chord.objects.filter(id__iexact =107)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Muskurane_Ki_Wajah_Tum_Ho_Guitar_Tabs___Lead___City_Lights___Abhijeet(request):
	text = chord.objects.filter(id__iexact =108)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Suno_Na_Sangemarmar_Guitar_Tabs___Youngistaan___Abhijeet(request):
	text = chord.objects.filter(id__iexact =109)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Humko_Humise_Chura_Lo_Guitar_Tabs___Lead___Mohabbatein_Tune___Abhijeet(request):
	text = chord.objects.filter(id__iexact =110)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kal_Ho_Naa_Ho_Guitar_Tabs___Lead___Title_Track___Abhijeet(request):
	text = chord.objects.filter(id__iexact =111)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Aaj_Phir_Tumpe_Pyar_Aaya_Hai_Guitar_Tabs___Lead___Hate_Story_2___Abhijeet(request):
	text = chord.objects.filter(id__iexact =112)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Main_Tenu_Samjhawan_Ki_Guitar_Tabs___Lead___Humpty_Sharma_Ki_Dulhania___Abhijeet(request):
	text = chord.objects.filter(id__iexact =113)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Aaj_Dil_Shayrana_Guitar_Tabs___Lead___Holiday___Abhijeet(request):
	text = chord.objects.filter(id__iexact =114)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Teri_Meri_Teri_Meri_Guitar_Tabs___Lead___Bodygaurd___Abhijeet(request):
	text = chord.objects.filter(id__iexact =115)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Chura_Liya_Hai_Tumne_Jo_Dil_Ko_Guitar_Tabs___Lead___Yaadon_Ki_Baarat___Abhijeet(request):
	text = chord.objects.filter(id__iexact =116)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Luka_Chuppi_Bahut_Huyi_Guitar_Tabs___Lead___Rang_De_Basanti___Abhijeet(request):
	text = chord.objects.filter(id__iexact =117)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Papa_Kehte_Hain_Bada_Naam_Karega_Guitar_Tabs___Lead___Abhijeet(request):
	text = chord.objects.filter(id__iexact =118)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tum_Dil_Ki_Dhadkan_Mein_Guitar_Tabs___Lead___Abhijeet(request):
	text = chord.objects.filter(id__iexact =119)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Dard_Dilo_Ke_Guitar_Tabs___Lead___The_Xpose___Abhijeet(request):
	text = chord.objects.filter(id__iexact =120)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Banjara_Guitar_Tabs___Lead___Ek_Villain___Abhijeet(request):
	text = chord.objects.filter(id__iexact =121)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def HUMDARD_Guitar_Tabs___Lead___Ek_Villain___Abhijeet(request):
	text = chord.objects.filter(id__iexact =122)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ishq_Wala_Love_Guitar_Tabs___Lead___Student_of_the_Year__SOTY____Abhijeet(request):
	text = chord.objects.filter(id__iexact =123)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tu_Hi_Tu_Har_Jagah_Guitar_Tabs___Lead___KICK__2014____Abhijeet(request):
	text = chord.objects.filter(id__iexact =124)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sandese_Aate_Hain_Guitar_Tabs___Lead___Border___Abhijeet(request):
	text = chord.objects.filter(id__iexact =125)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Happy_Birthday_To_You_Guitar_Tabs___Lead___Bday_Song_Tune___Abhijeet(request):
	text = chord.objects.filter(id__iexact =126)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Raghupati_Raghav_Raja_Ram_Guitar_Tabs___Lead___Ram_Bhajan___Abhijeet(request):
	text = chord.objects.filter(id__iexact =127)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tera_Hone_Laga_Hoon_Guitar_Tabs___Lead___Ajab_Prem_Ki_Ghazab_Kahani___Abhijeet(request):
	text = chord.objects.filter(id__iexact =128)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kaise_Mujhe_Tum_Mil_Gayi_Guitar_Tabs___Lead___Ghajini___Abhijeet(request):
	text = chord.objects.filter(id__iexact =129)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Hai_Dil_Ye_Mera_Guitar_Tabs___Lead___Hate_Story_2___Abhijeet(request):
	text = chord.objects.filter(id__iexact =130)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Jumme_Ki_Raat_Hai_Guitar_Tabs___Lead___Kick__2014____Abhijeet(request):
	text = chord.objects.filter(id__iexact =131)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tera_Naam_Doon_Guitar_Tabs___Lead___Its_Entertainment___Abhijeet(request):
	text = chord.objects.filter(id__iexact =132)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kabhi_Aayine_Pe_Guitar_Tabs___Lead__Aye_Khuda____Hate_Story_2___Abhijeet(request):
	text = chord.objects.filter(id__iexact =133)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sawan_Aaya_Hai_Guitar_Tabs___Lead___Creature_3D___Abhijeet(request):
	text = chord.objects.filter(id__iexact =134)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sukoon_Mila_Guitar_Tabs___Lead___Mary_Kom___Arijit_Singh___Abhijeet(request):
	text = chord.objects.filter(id__iexact =135)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Gulaabi_Aankhen_Jo_Teri_Dekhi_Guitar_Chords___The_Train__1970____Abhijeet(request):
	text = chord.objects.filter(id__iexact =136)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Papa_kehte_hain_bada_naam_karega_Guitar_Chords___Qayamat_Se_Qayamat_Tak___Abhijeet(request):
	text = chord.objects.filter(id__iexact =137)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Mera_Mann_Kehne_Laga_Guitar_Tabs___Lead___Nautanki_Saala___Abhijeet(request):
	text = chord.objects.filter(id__iexact =138)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Khushnuma_Guitar_Tabs___Lead___Suyyash_Rai___Abhijeet(request):
	text = chord.objects.filter(id__iexact =139)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Saanson_Ko_Jeene_Ka_Guitar_Tabs___Lead___Zid__2014____Abhijeet(request):
	text = chord.objects.filter(id__iexact =140)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Chaar_Kadam_Guitar_Tabs___Lead___PK_2014____Abhijeet(request):
	text = chord.objects.filter(id__iexact =141)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Are_Re_Are_Ye_Kya_Hua_Guitar_Tabs___Lead___Dil_To_Pagal_Hai___Abhijeet(request):
	text = chord.objects.filter(id__iexact =142)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Raja_Ko_Rani_Se_Pyaar_Ho_Gaya_Guitar_Tabs___Lead___Akele_Hum_Akele_Tum___Abhijeet(request):
	text = chord.objects.filter(id__iexact =143)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Lag_Ja_Gale_Guitar_Tabs___Lead___Woh_Kaun_Thi___Abhijeet(request):
	text = chord.objects.filter(id__iexact =144)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Wo_Lamhe_Wo_baatein_Guitar_Tabs___Lead___Atif_Aslam___Abhijeet(request):
	text = chord.objects.filter(id__iexact =145)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Bin_Tere__Reprise__Guitar_Tabs___Lead___I_Hate_Love_Stories___Abhijeet(request):
	text = chord.objects.filter(id__iexact =146)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Bikhra_Hoon_Main_Guitar_Tabs___Lead___Aadat__Jal_The_Band____Abhijeet(request):
	text = chord.objects.filter(id__iexact =147)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Baatein_Ye_Kabhi_Na_Guitar_Tabs___Lead___Khamoshiyan___Abhijeet(request):
	text = chord.objects.filter(id__iexact =148)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kya_Mujhe_Pyar_Hai_Guitar_Tabs___Lead___Woh_Lamhe___Abhijeet(request):
	text = chord.objects.filter(id__iexact =149)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def JEENA_JEENA_Guitar_Tabs___Lead___Badlapur__Atif_Aslam____Abhijeet(request):
	text = chord.objects.filter(id__iexact =150)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Pehli_Pehli_Baar_Mohabbat_Ki_Hai_Guitar_Tabs___Lead___Sirf_Tum___Abhijeet(request):
	text = chord.objects.filter(id__iexact =151)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Mitti_di_khushboo_Guitar_Tabs___Lead___Ayushmann_Khurrana___Abhijeet(request):
	text = chord.objects.filter(id__iexact =152)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Dheere_Dheere_Se_Guitar_Tabs___Lead___Aashiqui__1990____Abhijeet(request):
	text = chord.objects.filter(id__iexact =153)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ek_Ladki_Ko_Dekha_To_Aisa_Laga_Guitar_Tabs___Lead___1942_Love_Story___Abhijeet(request):
	text = chord.objects.filter(id__iexact =154)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Doorie_Sahi_Jaye_Na_Guitar_Tabs___Lead___Atif_Aslam___Abhijeet(request):
	text = chord.objects.filter(id__iexact =155)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Laila_Tu_Saamne_Kyun_Na_Aaye_Guitar_Tabs___Lead___Faridkot___Abhijeet(request):
	text = chord.objects.filter(id__iexact =156)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sooraj_Dooba_Hai_Yaaron_Guitar_Tabs___Lead___Roy___Abhijeet(request):
	text = chord.objects.filter(id__iexact =157)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tu_Chahiye_Guitar_Tabs___Lead___Bajrangi_Bhaijaan___Abhijeet(request):
	text = chord.objects.filter(id__iexact =158)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sawan_Ka_Mahina_Pawan_Kare_Guitar_Tabs___Lead___Milan___Abhijeet(request):
	text = chord.objects.filter(id__iexact =159)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Yaaron_Dosti_Badi_Hi_Haseen_Hai_Guitar_Tabs___Lead___k_k___Abhijeet(request):
	text = chord.objects.filter(id__iexact =160)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Humnava_Guitar_Tabs___Lead___Humari_Adhuri_Kahani___Abhijeet(request):
	text = chord.objects.filter(id__iexact =161)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Leke_Pehla_Pehla_Pyaar_Guitar_Tabs___Lead___CID__1956____Abhijeet(request):
	text = chord.objects.filter(id__iexact =162)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Mere_Saamne_Wali_Khidki_Mein_Guitar_Tabs___Lead___Padosan___Abhijeet(request):
	text = chord.objects.filter(id__iexact =163)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Agar_Tum_Mil_Jao_Guitar_Tabs___Lead___Zeher___Abhijeet(request):
	text = chord.objects.filter(id__iexact =164)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sajda_Guitar_Tabs___Lead___My_Name_Is_Khan___Abhijeet(request):
	text = chord.objects.filter(id__iexact =165)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Neele_Neele_Ambar_Par_Guitar_Tabs___Lead___Kalakaar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =166)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tere_Naina_Tere_Naina_Guitar_Tabs___Lead___My_Name_Is_Khan___Abhijeet(request):
	text = chord.objects.filter(id__iexact =167)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tera_Chehra_Guitar_Tabs___Lead___SANAM_TERI_KASAM___ARIJIT_SINGH___Abhijeet(request):
	text = chord.objects.filter(id__iexact =168)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Teri_Meri_Kahaani_Guitar_Tabs___Lead___Gabbar_is_Back___Arijit_Singh___Abhijeet(request):
	text = chord.objects.filter(id__iexact =169)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Chunar_Guitar_Tabs___Lead___ABCD_2___Abhijeet(request):
	text = chord.objects.filter(id__iexact =170)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Bolna_Guitar_Tabs___Lead____Kapoor_and_Sons__Arijit_Singh___Abhijeet(request):
	text = chord.objects.filter(id__iexact =171)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sun_Saathiya_Guitar_Tabs___Lead___ABCD_2__Any_Body_Can_Dance_2____Abhijeet(request):
	text = chord.objects.filter(id__iexact =172)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Rehnuma_Guitar_Tabs___Lead___ROCKY_HANDSOME___Abhijeet(request):
	text = chord.objects.filter(id__iexact =173)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Humari_Adhuri_Kahani_Guitar_Tabs___Lead___Arijit_Singh___Abhijeet(request):
	text = chord.objects.filter(id__iexact =174)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Baaton_Ko_Teri_Guitar_Tabs___Lead___All_is_Well___Abhijeet(request):
	text = chord.objects.filter(id__iexact =175)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tere_Bin_Nahi_Laage_Guitar_Tabs___Lead___Ek_Paheli_Leela___Abhijeet(request):
	text = chord.objects.filter(id__iexact =176)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Panchhi_Nadiya_Pawan_Ke_Jhonke_Guitar_Tabs___Lead___Refugee___Abhijeet(request):
	text = chord.objects.filter(id__iexact =177)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Deewani_Mastani_Guitar_Tabs___Lead___Bajirao_Mastani___Abhijeet(request):
	text = chord.objects.filter(id__iexact =178)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def List_of_Best_Bollywood_Hindi_Love_Songs___Valentine_Day_Songs___Abhijeet(request):
	text = chord.objects.filter(id__iexact =179)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Shreya_Ghoshal_Guitar_Tabs___Lead___Best_of_Shreya_Ghoshal___Abhijeet(request):
	text = chord.objects.filter(id__iexact =180)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Wafa_Ne_Bewafai_Guitar_tabs___Lead___Teraa_Suroor___Abhijeet(request):
	text = chord.objects.filter(id__iexact =181)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sab_Tera_Guitar_Tabs___Lead___BAAGHI___ARMAAN_MALIK__SHRADDHA_KAPOOR___Abhijeet(request):
	text = chord.objects.filter(id__iexact =182)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Main_Woh_Chaand_Guitar_Tabs___Lead___TERAA_SURROOR___Abhijeet(request):
	text = chord.objects.filter(id__iexact =183)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ijazat_Guitar_Tabs___Lead___ONE_NIGHT_STAND___ARIJIT_SINGH___Abhijeet(request):
	text = chord.objects.filter(id__iexact =184)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Bol_Do_Na_Zara_Guitar_Tabs___Lead___Azhar___Armaan_Malik___Abhijeet(request):
	text = chord.objects.filter(id__iexact =185)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Bekhudi_Guitar_Tabs___Lead___Teraa_Surroor___Darshan_Raval___Abhijeet(request):
	text = chord.objects.filter(id__iexact =186)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Yeh_Fitoor_Mera_Guitar_Tabs___Lead___Fitoor___Arijit_Singh___Abhijeet(request):
	text = chord.objects.filter(id__iexact =187)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Manwa_Behrupiya_Guitar_Tabs___Lead___Bollywood_Diaries___Abhijeet(request):
	text = chord.objects.filter(id__iexact =188)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Atrangi_Yaari_Guitar_Tabs___Lead___Wazir___Farhan_Akhtar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =189)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tere_Bin_Guitar_Tabs___Lead___Wazir___Sonu_Nigam___Abhijeet(request):
	text = chord.objects.filter(id__iexact =190)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sanam_Teri_Kasam_Guitar_Tabs___Lead___Ankit_Tiwari___Mohammed_Irfan___Abhijeet(request):
	text = chord.objects.filter(id__iexact =191)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Te_Amo_Guitar_Tabs___Lead___Dum_Maro_Dum___Ash_King___Sunidhi_Chauhan___Abhijeet(request):
	text = chord.objects.filter(id__iexact =192)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Phir_Mohabbat_Karne_Chala_Guitar_Tabs___Lead___Murder_2___Abhijeet(request):
	text = chord.objects.filter(id__iexact =193)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tujhse_Naraaz_Nahin_Zindagi_Guitar_Tabs___Lead___Masoom___Abhijeet(request):
	text = chord.objects.filter(id__iexact =194)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ambarsariya_Guitar_Tabs___Lead___Fukrey___Sona_Mohapatra___Abhijeet(request):
	text = chord.objects.filter(id__iexact =195)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Jabra_Fan_Guitar_Tabs___Lead___Fan___Nakash_Aziz___Abhijeet(request):
	text = chord.objects.filter(id__iexact =196)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Itni_Si_Baat_Hai_Guitar_Tabs___Lead___Azhar___Arijit_Singh___Abhijeet(request):
	text = chord.objects.filter(id__iexact =197)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Salamat_Guitar_Tabs___Lead___SARBJIT___ARIJIT_SINGH__TULSI_KUMAR___Abhijeet(request):
	text = chord.objects.filter(id__iexact =198)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Maninder_Buttar___Laare_Chords_with_Strumming_Pattern___Guitar___B_Praak___Jaani___Abhijeet(request):
	text = chord.objects.filter(id__iexact =199)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Easy_Capo___Vishal_Mishra___Teri_Hogaiyaan_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =200)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Easy___Unna_Nenachu_Chords_with_Strumming_Pattern___Psycho___Abhijeet(request):
	text = chord.objects.filter(id__iexact =201)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Easy___Armaan_Malik___Shaamein_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =202)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Easy_Baari_Chords_with_Strumming_Pattern___Bilaal___Momina_Mustehsan___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =203)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Easy___Yeh_Fitoor_Mera_Chords_with_Strumming_Pattern___Guitar____w_wo_Capo____Abhijeet(request):
	text = chord.objects.filter(id__iexact =204)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Easy___Mera_Mehboob_Chords___Stebin___Guitar___Awez_Darbar___Nagma_Mirajkar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =205)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Accurate___Ullaallaa_Chords_with_Strumming_Pattern___Guitar___Petta___Abhijeet(request):
	text = chord.objects.filter(id__iexact =206)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Jubin_Nautiyal___Main_Janta_Hoon_Chords_with_Strumming_Pattern___Easy___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =207)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Easy___Allah_Ve_Chords_with_Strumming_Pattern___Jassie_Gill___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =208)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Easy__Khuda_Hafiz_Chords_with_Strumming_Pattern___Guitar___The_Body___Abhijeet(request):
	text = chord.objects.filter(id__iexact =209)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tu_Hi_Yaar_Mera_Chords_with_Strumming_Pattern___Pati_Patni_Aur_Woh___Abhijeet(request):
	text = chord.objects.filter(id__iexact =210)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Bypass_Road___Easy___Tanha_Mera_Pyaar_Chords_with_Strumming_Pattern___Abhijeet(request):
	text = chord.objects.filter(id__iexact =211)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Easy___Good_Newwz__Maana_Dil_Chords_with_Strumming_Pattern___Guitar___B_Praak___Abhijeet(request):
	text = chord.objects.filter(id__iexact =212)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Arijit_Singh__Easy_Raanjhana_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =213)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Jubin_Nautiyal__Tujhe_Kitna_Chahein_Aur_Hum_Chords___Kabir_Singh__Film_Version____Abhijeet(request):
	text = chord.objects.filter(id__iexact =214)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ja_Chali_Ja_Guitar_Chords_with_Strumming_Pattern___Rishabh_Tiwari___Abhijeet(request):
	text = chord.objects.filter(id__iexact =215)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kabir_Singh___Guitar__Kaise_Hua_Chords_with_Strumming_Pattern___Abhijeet(request):
	text = chord.objects.filter(id__iexact =216)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Pehla_Pyaar_Chords_with_Strumming_Pattern__Guitar____Kabir_Singh___Abhijeet(request):
	text = chord.objects.filter(id__iexact =217)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Article_15__Intezari_Chords_with_Strumming_Pattern___Armaan_Malik___Abhijeet(request):
	text = chord.objects.filter(id__iexact =218)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Sajna_Ve_Chords_Lisa_Mishra___Vishal_Mishra_with_Strumming_Pattern___Abhijeet(request):
	text = chord.objects.filter(id__iexact =219)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Tere_Bin_Kive_Chords_with_Strumming___Ramji_Gulati___Jannat_Zubair___Mr__Faisu___Abhijeet(request):
	text = chord.objects.filter(id__iexact =220)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Super_30___Jugraafiya_Chords_with_Strumming_Pattern__Guitar____Abhijeet(request):
	text = chord.objects.filter(id__iexact =221)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Article_15__Naina_Yeh_Chords_with_Strumming_Pattern__Guitar____Abhijeet(request):
	text = chord.objects.filter(id__iexact =222)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Main_Tera_Ban_Jaunga_Chords_with_Strumming___Kabir_Singh__w_wo_Capo____Abhijeet(request):
	text = chord.objects.filter(id__iexact =223)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Malaal__Zara_Suno_Chords_with_Strumming_Pattern__Guitar____Abhijeet(request):
	text = chord.objects.filter(id__iexact =224)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Papon___Har_Lamhaa_Chords_with_Strumming_Pattern__Guitar____Abhijeet(request):
	text = chord.objects.filter(id__iexact =225)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Chehre_Padhna_Jaane_Naina___Matvaare_Chords_with_Strumming___Jubin___Abhijeet(request):
	text = chord.objects.filter(id__iexact =226)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Easy___Shawn_Mendes__Señorita_Guitar_Chords_with_Strumming_ft__Camila_Cabello___Abhijeet(request):
	text = chord.objects.filter(id__iexact =227)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Easy___Darshan_Raval___Tu_Mileya_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =228)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Dil_Diyan_Gallan_Guitar_Chords_with_Strumming___Tiger_Zinda_Hai___Abhijeet(request):
	text = chord.objects.filter(id__iexact =229)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Easy__Chukar_Mere_Man_Ko_Guitar_Chords_with_Strumming___Yaarana___Abhijeet(request):
	text = chord.objects.filter(id__iexact =230)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kidnap__Monta_Katha_Sonena_Guitar_Chords_with_Strumming___Abhijeet(request):
	text = chord.objects.filter(id__iexact =231)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Easy__Tujhe_Bhula_Diya_Guitar_Chords_with_Strumming__w_wo_Capo____Abhijeet(request):
	text = chord.objects.filter(id__iexact =232)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Mitti_Di_Khushboo_Guitar_Chords_with_Strum__w_wo_Capo____Abhijeet(request):
	text = chord.objects.filter(id__iexact =233)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Easy___Guitar__Nanhi_Pari_Chords_by_Sonu_Nigam__Asifa____Abhijeet(request):
	text = chord.objects.filter(id__iexact =234)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ankit_Tiwari_Guitar__Yeh_Tere_Do_Naina_Chords_with_Strumming_Pattern___Abhijeet(request):
	text = chord.objects.filter(id__iexact =235)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kabir_Singh__Tujhe_Kitna_Chahne_Lage_Chords_with_Strumming__w_wo_Guitar_Capo____Abhijeet(request):
	text = chord.objects.filter(id__iexact =236)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Easy__Tum_Ho_Guitar_Chords_with_Strumming__w_wo_Capo____Rockstar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =237)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def _Easy__Kabir_Singh__Mere_Sohneya_Guitar_Chords_with_Strumming_Pattern___Abhijeet(request):
	text = chord.objects.filter(id__iexact =238)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kidnap___Guitar__Ektu_Jayga_Dena_Chords_with_Strumming_Pattern___Abhijeet(request):
	text = chord.objects.filter(id__iexact =239)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Arijit_Singh__Bandeya_Guitar_Chords_with_Strumming___Dil_Junglee___Abhijeet(request):
	text = chord.objects.filter(id__iexact =240)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def _Easy__Bajrangi_Bhaijaan__Tu_Jo_Mila_Guitar_Chords_with_Strumming_Pattern___Abhijeet(request):
	text = chord.objects.filter(id__iexact =241)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Humne_Rait_Pe_Chords_with_Strum___Guitar___Neha_Kakkar___Tony_Kakkar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =242)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Zindagi_Di_Paudi_Guitar_Chords_with_Strumming___Millind_Gaba___Abhijeet(request):
	text = chord.objects.filter(id__iexact =243)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Royee_Jande_Naina_Guitar_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =244)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kabira_Guitar_Chords_from_Yeh_Jawaani_Hai_Deewani___Abhijeet(request):
	text = chord.objects.filter(id__iexact =245)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Maa_Guitar_Chords_by_Amitabh_Bachchan___Yajat___Abhijeet(request):
	text = chord.objects.filter(id__iexact =246)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Student_of_the_Year_2__Fakira_Guitar_Chords_with_Capo_by_Sanam___Abhijeet(request):
	text = chord.objects.filter(id__iexact =247)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def RAETH__Bhula_Do_Bhula_Do_Guitar_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =248)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Yaariyaan___Meri_Maa_Guitar_Chords_with_Strum__Two_Versions_Easy____Abhijeet(request):
	text = chord.objects.filter(id__iexact =249)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ami_Tomake_Bhalobashi_Guitar_Chords___KIDNAP___Abhijeet(request):
	text = chord.objects.filter(id__iexact =250)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Chal_Para_Chords_by_Strings_Band__Guitar_Piano_Ukulele____Abhijeet(request):
	text = chord.objects.filter(id__iexact =251)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kabir_Singh_Guitar__Bekhayali_Chords_with_Strumming__Updated____Abhijeet(request):
	text = chord.objects.filter(id__iexact =252)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Anxiety_Chords_by_Selena_Gomez___Julia_Michaels___Abhijeet(request):
	text = chord.objects.filter(id__iexact =253)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ankit_Tiwari___Guitar__Ishq_Kare_Barbadiyaan_Chords_with_Strumming___Abhijeet(request):
	text = chord.objects.filter(id__iexact =254)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Indias_Most_Wanted___Guitar__Akela_Chords_with_Strumming___Abhijeet(request):
	text = chord.objects.filter(id__iexact =255)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Dil_Royi_Jaye_Chords_with_Strumming___Guitar___De_De_Pyar_De___Abhijeet(request):
	text = chord.objects.filter(id__iexact =256)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Aaradhana_Ho_Aaradhana_Guitar_Chords___Worship___Abhijeet(request):
	text = chord.objects.filter(id__iexact =257)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Papon___Guitar__Ik_Mod_Chords_with_Strumming_Pattern___Music_Teacher___Abhijeet(request):
	text = chord.objects.filter(id__iexact =258)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Main_Bhi_Nahin_Soya_Guitar_Chords___SOTY_2___Abhijeet(request):
	text = chord.objects.filter(id__iexact =259)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Music_Teacher__Sambhaal_Rakhiyaan_Chords___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =260)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Mere_Aas_Paas_Chords___Guitar_by_Yasser_Desai___Abhijeet(request):
	text = chord.objects.filter(id__iexact =261)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tu_Mila_to_Haina_Chords_with_Capo___Strumming___Guitar___De_De_Pyar_De___Abhijeet(request):
	text = chord.objects.filter(id__iexact =262)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Aaj_Se_Teri_Guitar_Chords_with_Strumming___PADMAN___Abhijeet(request):
	text = chord.objects.filter(id__iexact =263)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Linkin_Park_Numb_Guitar_Chords_with_Capo___Strumming__Easy____Abhijeet(request):
	text = chord.objects.filter(id__iexact =264)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Somebody_s_Guitar_Chords_with_Capo___Strumming___Enrique_Iglesias___Abhijeet(request):
	text = chord.objects.filter(id__iexact =265)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def EASY___Teri_Khaamiyan_Guitar_Chords_with_Strumming___Abhijeet(request):
	text = chord.objects.filter(id__iexact =266)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def EASY__Tum_Hi_Ho_Guitar_Chords_with_Capo__Strumming___Lead___Abhijeet(request):
	text = chord.objects.filter(id__iexact =267)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tujhko_Jo_Paaya_Mere_Bina_Guitar_Chords_with_Strumming___Capo___CROOK___Abhijeet(request):
	text = chord.objects.filter(id__iexact =268)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Muskurane_Ki_Wajah_Guitar_Chords_with_Strumming__Easy____Abhijeet(request):
	text = chord.objects.filter(id__iexact =269)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def EASY__Mere_Mehboob_Qayamat_Hogi_Guitar_Chords_with_Strumming___Abhijeet(request):
	text = chord.objects.filter(id__iexact =270)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Mon_Aamar_Chords_by_Arko___Shesh_Theke_Shuru___Abhijeet(request):
	text = chord.objects.filter(id__iexact =271)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ishqe_Di_Chashni_Guitar_Chords___Strum___Bharat___Salman_Khan___Abhijeet(request):
	text = chord.objects.filter(id__iexact =272)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Chale_Aana_Chords_with_Capo_by_Armaan_Malik___Dede_Pyar_De___Abhijeet(request):
	text = chord.objects.filter(id__iexact =273)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Dhvani_Bhanushali___Guitar__Vaaste_Chords_with_Strumming___Abhijeet(request):
	text = chord.objects.filter(id__iexact =274)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Tu_Thodi_Der_Chords_with_Capo___Strumming___Half_Girlfriend___Abhijeet(request):
	text = chord.objects.filter(id__iexact =275)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Music_Teacher___Guitar__Phir_Wahi_Raat_Hai_Chords_with_Strumming___Abhijeet(request):
	text = chord.objects.filter(id__iexact =276)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitra__Roke_Na_Ruke_Naina_Chords_with_Capo__Strumming____Abhijeet(request):
	text = chord.objects.filter(id__iexact =277)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Maa_Chords_by_Ankit_Tiwari___Abhijeet(request):
	text = chord.objects.filter(id__iexact =278)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def KALANK___Guitar__Tabaah_Ho_Gaye_Guitar_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =279)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Yasser_Desari___Guitar__Meri_Hasi_Chords_with_Strumming___Abhijeet(request):
	text = chord.objects.filter(id__iexact =280)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Pora_Mon_Chords_with_Strumming__Easy____Ke_Tumi_Nandini___Abhijeet(request):
	text = chord.objects.filter(id__iexact =281)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Title_Track___Guitar__Shudhu_Tomari_Jonno_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =282)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Aur_Kuch_Baki_Chords_by_Yasser_Desai___Abhijeet(request):
	text = chord.objects.filter(id__iexact =283)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Eka_Ekela_Mon_Guitar_Chords___Chirodini_Tumi_Je_Amar_2___Abhijeet(request):
	text = chord.objects.filter(id__iexact =284)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Dosti_Guitar_Chords_with_Strumming_from_Junglee___Abhijeet(request):
	text = chord.objects.filter(id__iexact =285)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Bastushaap___Tomake_Chuye_Dilam_Guitar_Chords___Arijit_Singh___Abhijeet(request):
	text = chord.objects.filter(id__iexact =286)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def A_Star_Is_Born___SHALLOW_Guitar_Chords_by_Lady_Gaga___Bradley_Cooper___Abhijeet(request):
	text = chord.objects.filter(id__iexact =287)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Amake_Amar_Moto_Thakte_Dao_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =288)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Shaan___Guitar__Tu_Mera_Rab_Hai_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =289)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sweater___Guitar__Preme_Pora_Baron_Chords__Strumming____Bengali___Abhijeet(request):
	text = chord.objects.filter(id__iexact =290)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def MS_Dhoni___Guitar__Kaun_Tujhe_Chords__Easy____Abhijeet(request):
	text = chord.objects.filter(id__iexact =291)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def OK_Jaanu___Guitar__Enna_Sona_Chords_by_Arijit_Singh__Strumming____Abhijeet(request):
	text = chord.objects.filter(id__iexact =292)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def CYPHER___Guitar__Meri_Maa_Chords_by_Sonu_Nigam___Abhijeet(request):
	text = chord.objects.filter(id__iexact =293)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def RAW___Guitar__Bulleya_Chords_by_Rabbi_Shergill___Abhijeet(request):
	text = chord.objects.filter(id__iexact =294)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def RAW___Guitar__Jee_Len_De_Chords_by_Mohit_Chauhan__Strumming____Abhijeet(request):
	text = chord.objects.filter(id__iexact =295)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def QARAN___Guitar__Haaye_Oye_Chords_ft__Ash_King__Strum____Abhijeet(request):
	text = chord.objects.filter(id__iexact =296)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Chala_Jata_Hoon_Guitar_Chords_by_Sanam_Puri___Abhijeet(request):
	text = chord.objects.filter(id__iexact =297)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Arijit_Singh___Guitar__Kalank_Guitar_Chords_with_Strumming___Title_Track___Abhijeet(request):
	text = chord.objects.filter(id__iexact =298)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Junglee___Guitar__Fakeera_Ghar_Aaja_Chords___Jubin_Nautiyal___Abhijeet(request):
	text = chord.objects.filter(id__iexact =299)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def GUITAR__Sun_Mere_Humsafar_Chords_with_Strumming___Badrinath_Ki_Dulhania___Abhijeet(request):
	text = chord.objects.filter(id__iexact =300)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Half_Girlfriend___Guitar__Main_Phir_Bhi_Tumko_Chahunga_Chords__w_wo_Capo____Abhijeet(request):
	text = chord.objects.filter(id__iexact =301)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Jubin_Nautiyal___Guitar__Chitthi_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =302)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Duniyaa_Chords_with_Strumming_Pattern___Luka_Chuppi___Abhijeet(request):
	text = chord.objects.filter(id__iexact =303)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Mere_Pyare_Prime_Minister_Chords___Title_Track___Abhijeet(request):
	text = chord.objects.filter(id__iexact =304)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def KK___Guitar__Tum_Na_Aaye_Chords___Badla___Abhijeet(request):
	text = chord.objects.filter(id__iexact =305)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def BB_Ki_Vines___Guitar__Bas_Mein_Chords___Bhuvan_Bam___Abhijeet(request):
	text = chord.objects.filter(id__iexact =306)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Arijit_Singh___Guitar__Ruan_Ruan_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =307)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Mohit_Chauhan___Guitar__Safar_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =308)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Notebook___Guitar__Laila_Chords___Dhavani_Bhanushali___Abhijeet(request):
	text = chord.objects.filter(id__iexact =309)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Total_Dhamaal___Guitar__Mungda_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =310)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Darshan_Raval___Guitar__Kaash_Aisa_Hota_Chords__w_wo_Capo____Abhijeet(request):
	text = chord.objects.filter(id__iexact =311)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Arko___Guitar__Shukriya_Chords___Shokhsanam___Abhijeet(request):
	text = chord.objects.filter(id__iexact =312)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kalank___Guitar__Ghar_More_Pardesiya_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =313)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kesari__Ve_Maahi_Guitar_Chords_with_Strumming_Pattern___Arijit_Singh___Abhijeet(request):
	text = chord.objects.filter(id__iexact =314)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kesari_Guitar__Teri_Mitti_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =315)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Notebook___Guitar__Main_Taare_Chords_by_Salman_Khan__Strumming____Abhijeet(request):
	text = chord.objects.filter(id__iexact =316)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Luka_Chuppi___Guitar__Photo_Chords_with_Capo___Abhijeet(request):
	text = chord.objects.filter(id__iexact =317)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Mujhse_Kaha_Naa_Gaya_Chords___Palash_Sen___Abhijeet(request):
	text = chord.objects.filter(id__iexact =318)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Teri_Yaad_Chords___Rahat_Fateh_Ali_Khan___Abhijeet(request):
	text = chord.objects.filter(id__iexact =319)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Arko___Guitar__Shukriya_Chords_with_Capo___Abhijeet(request):
	text = chord.objects.filter(id__iexact =320)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Neha_Kakkar__Tera_Ghata_Chords___Guitar_Version___Abhijeet(request):
	text = chord.objects.filter(id__iexact =321)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Tujhe_Kaise_Pata_Na_Chala_Chords__Reprise____Asees_Kaur___Abhijeet(request):
	text = chord.objects.filter(id__iexact =322)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Tu_Meri_Zindagi_Chords_by_Keshav_Kumar___Rohan_Mehra___Abhijeet(request):
	text = chord.objects.filter(id__iexact =323)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Atif_Aslam___Guitar__Baarishein_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =324)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Jibon_Re_Chords___Prem_Amar_2___Abhijeet(request):
	text = chord.objects.filter(id__iexact =325)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Ek_Galti_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =326)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Notebook___Guitar__Nai_Lagda_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =327)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Dilbar_Mere_Guitar_Chords___1982___Abhijeet(request):
	text = chord.objects.filter(id__iexact =328)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Do_Lafzon_Ki_Hai_Guitar_Chords___The_Great_Gambler___Abhijeet(request):
	text = chord.objects.filter(id__iexact =329)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Mohit_Chauhan___Guitar__Kyun_Dil_Mera_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =330)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Dhavni_Bhanushali__Leja_Leja_Re_Guitar_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =331)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Song_Nigam__Marham_Chords___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =332)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Band___Strings__Piya_Re_Guitar_Chords___Cornetto___Abhijeet(request):
	text = chord.objects.filter(id__iexact =333)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Naino_Ki_To_Baat_Chords___Mera_Sanam___Abhijeet(request):
	text = chord.objects.filter(id__iexact =334)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Phir_Se___Guitar__Maine_Socha_Ke_Chura_Loon_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =335)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Band___Strings__Mil_Gaya_Chords___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =336)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Jass_Gujral__Aa_bhi_Ja_Chords___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =337)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Teri_Galliyan_Chords__Unplugged_Acoustic____Abhijeet(request):
	text = chord.objects.filter(id__iexact =338)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Armaan_Malik___Zikr_Chords_with_Intro_Tabs___Guitar__Amavas____Abhijeet(request):
	text = chord.objects.filter(id__iexact =339)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Darshan_Raval__Bhula_Diya_Chords___Lyrics___Guitar__With_Strumming____Abhijeet(request):
	text = chord.objects.filter(id__iexact =340)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Amavas___Guitar__Dhadkan_Chords_by_Jubin_Nautiyal___Palak_Muchhal___Abhijeet(request):
	text = chord.objects.filter(id__iexact =341)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Tu_Karde_Haan_Chords___Akhil__with___without_Capo____Abhijeet(request):
	text = chord.objects.filter(id__iexact =342)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Dhvani_Bhanushali__Main_Teri_Hoon_Chords___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =343)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Tum_Mere_Ho_Chords___Vivek_Singh__Pehchaan_Music____Abhijeet(request):
	text = chord.objects.filter(id__iexact =344)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Tum_Aisi_Kyun_Ho_Chords___Hum_Chaar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =345)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Barf_Si_Tu_Pighal_Ja_Chords___Armaan_Malik___Abhijeet(request):
	text = chord.objects.filter(id__iexact =346)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Darshan_Raval__Ek_Ladki_Ko_Dekha_To_Aisa_Laga_Guitar_Chords__Reprise____Abhijeet(request):
	text = chord.objects.filter(id__iexact =347)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Bheege_Bheege_Chords___Ankit_Tiwari__Sunidhi_Chauhan__Amavas____Abhijeet(request):
	text = chord.objects.filter(id__iexact =348)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Why_Cheat_India___Guitar__Tu_Kitna_Kaamyaab_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =349)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Hum_Chaar___Guitar__Manmeet_Mere_Chords___Mohit_Chauhan___Abhijeet(request):
	text = chord.objects.filter(id__iexact =350)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Khwaaish_Chords___Sajan_Patel___Abhijeet(request):
	text = chord.objects.filter(id__iexact =351)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Chehre_Chords___Harish_Verma__Punjabi____Abhijeet(request):
	text = chord.objects.filter(id__iexact =352)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Kaise_Bhuloon_Chords___Gurnazar_Chattha___Abhijeet(request):
	text = chord.objects.filter(id__iexact =353)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Bairiya_Chords___Bombairiya___Arko___Abhijeet(request):
	text = chord.objects.filter(id__iexact =354)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Ye_Pyaar_Nahi_To_Kya_Hai_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =355)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Tu_Na_Mera_Chords___Arjun_Kanungo___Abhijeet(request):
	text = chord.objects.filter(id__iexact =356)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Baarishein_Chords___Ankit_Rajput___Shivangi_Bhayana___Abhijeet(request):
	text = chord.objects.filter(id__iexact =357)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Fraud_Saiyaan___Guitar__Ishq_Ishq_Tera_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =358)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Tanha_Hua_Chords___Zero___Rahat_Fateh_Ali_Khan___Abhijeet(request):
	text = chord.objects.filter(id__iexact =359)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Lae_Dooba_Chords___Aiyaary__w_wo_Capo____Abhijeet(request):
	text = chord.objects.filter(id__iexact =360)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Alvida_Alvida_Chords___Little_Boy___Sonu_Nigam___Abhijeet(request):
	text = chord.objects.filter(id__iexact =361)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Toke_Chara_Chords___Jubin_Nautiyal___Abhijeet(request):
	text = chord.objects.filter(id__iexact =362)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Ann_Bann_Chords___Zero___Kunal_Ganjawala___Abhijeet(request):
	text = chord.objects.filter(id__iexact =363)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Jind_Mahi_Chords___Diljit_Dosanjh___Abhijeet(request):
	text = chord.objects.filter(id__iexact =364)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Dil_Mein_Ho_Tum_Chords_by_Armaan_Malik___Why_Cheat_India___Abhijeet(request):
	text = chord.objects.filter(id__iexact =365)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Simmba__New_Tere_Bin_Guitar_Chords___Rahat_Fateh_Ali_Khan___Abhijeet(request):
	text = chord.objects.filter(id__iexact =366)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Mahi_Aaja_Chords___Asim_Azhar_ft__Momina_Mustehsan___Abhijeet(request):
	text = chord.objects.filter(id__iexact =367)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Behe_Chala_Chords___Yaseer_Desai__Shashwat_Sachdev___Abhijeet(request):
	text = chord.objects.filter(id__iexact =368)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Billian_Billian_Chords___Guri___Abhijeet(request):
	text = chord.objects.filter(id__iexact =369)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Why_Cheat_India__Phir_Mulaaqat_Chords___Guitar___Jubin_Nautiyal___Abhijeet(request):
	text = chord.objects.filter(id__iexact =370)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Fikar_Chords___Rahat_Fateh_Ali_Khan___Neha_Kakkar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =371)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Yasser_Desai___Tum_Chale_Gaye_Chords___Marudhar_Express___Abhijeet(request):
	text = chord.objects.filter(id__iexact =372)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Jo_Tu_Na_Mila_Chords___Asim_Azhar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =373)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Sakhiyaan_Chords___Maninder_Buttar___Babbu___Abhijeet(request):
	text = chord.objects.filter(id__iexact =374)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Teen_Cup_Chaa_Chords___Title_Track___Subho_Pramanik___Abhijeet(request):
	text = chord.objects.filter(id__iexact =375)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Jaan_Nisaar_Chords__w_wo_Capo___Strumming____Kedarnath___Abhijeet(request):
	text = chord.objects.filter(id__iexact =376)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Soham_Naik___Tum_Aaoge_Chords__w_wo_Capo___Strumming_Pattern____Abhijeet(request):
	text = chord.objects.filter(id__iexact =377)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Mera_Pyar_Tera_Pyar_Chords__w_wo_Capo___Strumming____Abhijeet(request):
	text = chord.objects.filter(id__iexact =378)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Tere_Te_Chords___Guru_Randhawa___Abhijeet(request):
	text = chord.objects.filter(id__iexact =379)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Tu_Hi_Re_Chords___Armaan_Malik___Abhijeet(request):
	text = chord.objects.filter(id__iexact =380)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Pinjra_Chords___Gurnazar__w_wo_Capo___Strumming____Abhijeet(request):
	text = chord.objects.filter(id__iexact =381)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Mamla_Dil_Da_Chords___Tonny_Kakkar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =382)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Bhaagte_Raho___Guitar__Gum_Hoon_Chords___Yasser_Desai___Abhijeet(request):
	text = chord.objects.filter(id__iexact =383)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Manush_Ekhono_Manusher_Pashe_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =384)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Mujhe_Kaise_Pata_Na_Chala_Chords___Papon___Abhijeet(request):
	text = chord.objects.filter(id__iexact =385)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sweetheart_Guitar_Chords___Kedarnath___Dev_Negi___Abhijeet(request):
	text = chord.objects.filter(id__iexact =386)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Tere_Jisam_Chords_with_Strumming_Pattern___Altaaf_Sayyed___Abhijeet(request):
	text = chord.objects.filter(id__iexact =387)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Naina_Chords_by_Ankit_Tiwari___Abhijeet(request):
	text = chord.objects.filter(id__iexact =388)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Nazm_Nazm_Chords__Two_versions____Abhijeet(request):
	text = chord.objects.filter(id__iexact =389)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Meray_Saathiya_Chords___Roxen___Mustafa_Zahid___Abhijeet(request):
	text = chord.objects.filter(id__iexact =390)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Tera_Yaar_Hoon_Main_Chords___Arijit_Singh__w_wo_Capo____Abhijeet(request):
	text = chord.objects.filter(id__iexact =391)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Tu_Kareeb_Aaya_Chords___Rishabh_Srivastava___Aakanksha_Sharma___Abhijeet(request):
	text = chord.objects.filter(id__iexact =392)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Akhia_Di_Bhatkan_Chords___Sharry_Mann___Abhijeet(request):
	text = chord.objects.filter(id__iexact =393)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Sunn_Le_Zara_Chords___Arnab_Dutta___1921___Abhijeet(request):
	text = chord.objects.filter(id__iexact =394)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Allah_Duhai_Hai_Chords___Zayn___Abhijeet(request):
	text = chord.objects.filter(id__iexact =395)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Qaafirana_Chords_with_Strumming___Arijit_Singh___Kedarnath___Abhijeet(request):
	text = chord.objects.filter(id__iexact =396)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Sapna_Chords_with_Strumming_Pattern___Arijit_Singh___Abhijeet(request):
	text = chord.objects.filter(id__iexact =397)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Mere_Naam_Tu_Chords_with_Strumming_Pattern___Zero___Abhijeet(request):
	text = chord.objects.filter(id__iexact =398)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Aawargi_Chords_with_Strumming_Pattern___Jubin_Nautiyal___Abhijeet(request):
	text = chord.objects.filter(id__iexact =399)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Mein_Adhura_Lafz_Chords_with_Strumming_Pattern___Baazaar___Rahat_Fateh_Ali_Khan___Abhijeet(request):
	text = chord.objects.filter(id__iexact =400)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Dil_Zaffran_Chords_with_Strumming_Pattern___Rahat_Fateh_Ali_Khan___Abhijeet(request):
	text = chord.objects.filter(id__iexact =401)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Pagal_Chords_by_Diljit_Dosanjh__Strumming____Abhijeet(request):
	text = chord.objects.filter(id__iexact =402)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Zindagi_Mil_Jayegi_Chords___Tony___Neha_Kakkar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =403)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Teri_Judai_Mein_Chords_by_Hukam_Ali___Abhijeet(request):
	text = chord.objects.filter(id__iexact =404)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Baaki_Hai_Chords_with_Strumming_Pattern___Sonu_Nigam___5_Weddings___Abhijeet(request):
	text = chord.objects.filter(id__iexact =405)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Siren_Chords_by_The_Chainsmokers___Aazar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =406)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__If_I_Say_Chords_by_Mumford___Sons___Abhijeet(request):
	text = chord.objects.filter(id__iexact =407)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Got_My_Name_Changed_Back_Chords___Pisot_Annies___Abhijeet(request):
	text = chord.objects.filter(id__iexact =408)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Namo_Namo_Chords___Kedarnath___Abhijeet(request):
	text = chord.objects.filter(id__iexact =409)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Baarish_Chords_by_Neha_Kakkar___Bilal_Saeed___Abhijeet(request):
	text = chord.objects.filter(id__iexact =410)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Dil_Mastiyaan_Chords___Ash_King___Payal_Dev___Abhijeet(request):
	text = chord.objects.filter(id__iexact =411)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Kya_Baat_Ay_Chords_with_Strumming_Pattern___Hardy_Sandhu___Abhijeet(request):
	text = chord.objects.filter(id__iexact =412)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Bhaiji__Do_Naina_Chords_with_Strumming_Pattern___Yasser_Desai_Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =413)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Jaane_Ye_Kyun_Kiya_Chords_with_Strumming_Pattern___Farhan_Akhtar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =414)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Nain_Na_Jodi_Chords_with_Strumming_Pattern___Ayushmann_Khurrana___Abhijeet(request):
	text = chord.objects.filter(id__iexact =415)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Arijit_Singh__Dooba_Dooba_Chords_with_Strumming_Pattern___Guitar__Helicopter_Eela____Abhijeet(request):
	text = chord.objects.filter(id__iexact =416)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def KK__Pehle_Ke_Jaisa_Chords_with_Strumming_Pattern___Jalebi_Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =417)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Iktara_Chords_with_Strumming_Pattern___Wake_Up_Sid___Abhijeet(request):
	text = chord.objects.filter(id__iexact =418)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Dooba_Dooba_Chords_by_Sanam_Puri___Silk_Route__Strumming____Abhijeet(request):
	text = chord.objects.filter(id__iexact =419)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Chhod_Diya_Chords_with_Strumming_Pattern___Baazaar___Arijit_Singh___Abhijeet(request):
	text = chord.objects.filter(id__iexact =420)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Fakira_Chords_by_Gurnam_Bhullar___Qismat___Abhijeet(request):
	text = chord.objects.filter(id__iexact =421)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Soch_Na_Sake_Guitar_Chords_with_Strumming_Pattern___Airlift_Arijit_Singh___Abhijeet(request):
	text = chord.objects.filter(id__iexact =422)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Atif__Tere_Liye_Chords_with_Strumming_Pattern___Guitar___Namaste_England___Abhijeet(request):
	text = chord.objects.filter(id__iexact =423)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Arijit_Singh__Pal_Chords_with_Strumming_Pattern__Capo_Non_Capo____Guitar___Jalebi___Abhijeet(request):
	text = chord.objects.filter(id__iexact =424)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Arijit_Singh__Har_Har_Gange_Chords___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =425)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Tum_Se_Chords_with_Strumming_Pattern__Capo____Jubin_Nautiyal_Jalebi___Abhijeet(request):
	text = chord.objects.filter(id__iexact =426)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Darshan_Raval__Do_Din_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =427)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar__Naina_Da_Kya_Kasoor_Chords_with_Strumming_Pattern___Andhadhun___Abhijeet(request):
	text = chord.objects.filter(id__iexact =428)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Aap_Se_Milkar_Chords_with_Strumming_Pattern_Ayushmann_Khurrana___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =429)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Le_Ja_Tu_Kahin_Chords_with_Strumming_Pattern___Arijit_Singh_Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =430)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Aye_Zindagi_Chords_with_Strumming_Pattern___Sonu_Nigam_Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =431)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Arijit__Woh_Ladki_Chords_with_Strumming_Pattern___Andhadhun_Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =432)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Doorie_Chords_with_Strumming_Pattern___Benjamin_Rohan_Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =433)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Mitron__Door_Na_Ja_Chords_with_Strumming_Pattern___Abhijeet(request):
	text = chord.objects.filter(id__iexact =434)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Atif_Aslam__Tum_Chords_with_Strumming_Pattern___Laila_Majnu_Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =435)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Jubin_Nautiyal___Sawarne_Lage_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =436)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def F_For_Fyaar_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =437)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Easy_Neele_Neele_Ambar_Par_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =438)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Arijit_Singh___Aahista_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =439)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Nazar_Na_Lag_Jaaye_Chords_with_Strumming_Pattern___Guitar___Ash_King___Abhijeet(request):
	text = chord.objects.filter(id__iexact =440)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Promises_Chords_with_Strumming_Pattern___Guitar___Sam_Smith__Calvin_Harris___Abhijeet(request):
	text = chord.objects.filter(id__iexact =441)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sochta_Hoon___Dekhte_Dekhte_Chords___Guitar__with_Capo___without_Capo____Atif_Aslam___Abhijeet(request):
	text = chord.objects.filter(id__iexact =442)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Atif_Aslam___Chalte_Chalte_Chords_with_Strumming_Pattern__Easy____Abhijeet(request):
	text = chord.objects.filter(id__iexact =443)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sanam_Puri___Bheegi_Bheegi_Raaton_Mein_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =444)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Atif_Aslam_Tera_Hua_Chords_with_Strumming_Pattern___Loveratri___Abhijeet(request):
	text = chord.objects.filter(id__iexact =445)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Fanney_Khan___Tere_Jaisa_Tu_Chords_With_strumming_Pattern__Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =446)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tujhse_Naraz_Nahi_Zindagi_Chords_With_Strumming_Pattern___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =447)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Hamza_Malik___O_Jaana_Chords_with_Strumming_Pattern_by_Rahat_Fateh_Ali_Khan___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =448)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Atif_Aslam___Jeena_Jeena_Chords_with_Strumming_Pattern___Guitar___Badlapur___Abhijeet(request):
	text = chord.objects.filter(id__iexact =449)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar___Easy_Happy_Birthday_Chords_with_Strumming_Pattern__Multiple_Version____Abhijeet(request):
	text = chord.objects.filter(id__iexact =450)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def David_Guetta___Dont_Leave_Me_Alone_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =451)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Arijit_Singh___Andheron_Mein_Rishtey_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =452)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Satyameva_Jayate___Tere_Jaisa_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =453)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sabrina_Claudio___Messages_From_Her_Chords___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =454)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kya_Hua_Tera_Wada_Chords_with_Strumming_Pattern___Guitar___Old_Song___Abhijeet(request):
	text = chord.objects.filter(id__iexact =455)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def _Idiots___Give_Me_Some_Sunshine_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =456)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Chura_Liya_Hai_Tumne_Jo_Dil_Ko_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =457)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Mere_Samne_Wali_Khidki_Mein_Chords_with_Strumming_Pattern___Guitar___Old_Song___Abhijeet(request):
	text = chord.objects.filter(id__iexact =458)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Gold___Naino_Ne_Baandhi_Piano_Notes___Abhijeet(request):
	text = chord.objects.filter(id__iexact =459)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Darshan_Raval___Baarish_Lete_Aana_Piano_Notes___Abhijeet(request):
	text = chord.objects.filter(id__iexact =460)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Naino_Ne_Baandhi_Chords___Guitar___Mouni_Roy___Akshay_Kumar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =461)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Pehli_baar_Dhadak_Chords_With_Capo_and_Strumming_Pattern___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =462)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sunidhi_Chauhans_Mohabbat_Chords_With_Strumming_Pattern___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =463)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Pehli_Baar_Piano_Notes___Dhadak___Jhanvi_Kapoor___Ishaan___Abhijeet(request):
	text = chord.objects.filter(id__iexact =464)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Arijit_Singh___Tera_Fitoor_Chords_With_Strumming_Pattern___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =465)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Dhadak___Pehli_Baar_Chords_With_Strumming_Pattern___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =466)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Atif_Aslam___Paniyo_Sa_Chords_With_Strumming_Pattern___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =467)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Fanney_Khan___Halka_Halka_Chords_With_Strumming_Pattern___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =468)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Karwaan___Saansein_Chords_With_Strumming_Pattern___Guitar___Prateek_Khulad___Abhijeet(request):
	text = chord.objects.filter(id__iexact =469)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Chori_Chori_Jab_Nazrein_Mili_Chords_With_Strumming_Pattern_Guitar___Namita___Abhijeet(request):
	text = chord.objects.filter(id__iexact =470)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Darshan_Raval___Baarish_Lete_Aana_Chords_With_Strumming_Pattern___With_Without_Capo___Abhijeet(request):
	text = chord.objects.filter(id__iexact =471)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Asees_Zaroorat_Chords_With_Strumming_Pattern___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =472)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Janhvi_Kapoor___Dhadak_Title_Track_Chords___Guitar__First_Song____Abhijeet(request):
	text = chord.objects.filter(id__iexact =473)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def SANJU___Ruby_Ruby_Chords___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =474)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kyun_Na_Mere_Chords___Guitar___Rishabh_Srivastava___Abhijeet(request):
	text = chord.objects.filter(id__iexact =475)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kanth_Kaler___Silsila_Chords___Guitar__Punjabi_Song____Abhijeet(request):
	text = chord.objects.filter(id__iexact =476)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Param_Singh___Jhanjar_Chords___Guitar___Punjabi_Song___Abhijeet(request):
	text = chord.objects.filter(id__iexact =477)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Geeta_Zaildar___Jeen_Nu_Chords___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =478)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ahida_Chords___Guitar___Shyamoli_Singh__Ravi_Singhal___Abhijeet(request):
	text = chord.objects.filter(id__iexact =479)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kuch_Iss_Tarah_Chords_With_Strumming_Pattern___Guitar_1921___Zareen_Khan___Abhijeet(request):
	text = chord.objects.filter(id__iexact =480)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ayushmann_Khurrana___Chan_Kitthan_Chords_With_Strumming___Guitar____Abhijeet(request):
	text = chord.objects.filter(id__iexact =481)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Akhil___Rang_Gora_Chords_With_Strumming_Pattern___Guitar__Punjabi____Abhijeet(request):
	text = chord.objects.filter(id__iexact =482)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Satyameva_Jayate___Dilbar_Chords___Guitar___Neha_Kakkar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =483)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Baaghi_2___O_Saathi_Chords_Without_Capo__Guitar____Atif_Aslam___Abhijeet(request):
	text = chord.objects.filter(id__iexact =484)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Papa_Kehte_Hain_Chords_With_Strumming___Qayamat_Se_Qayamat_Tak___Udit_Narayan___Abhijeet(request):
	text = chord.objects.filter(id__iexact =485)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Bhuvan_Bam___Safar_Guitar_Chords_With_Strumming_Pattern__BB_Ki_Vines____Abhijeet(request):
	text = chord.objects.filter(id__iexact =486)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guri___Jaan_Guitar_Chords___ALBUM_26___Abhijeet(request):
	text = chord.objects.filter(id__iexact =487)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kar_Har_Maidaan_Fateh_Chords___SANJU__With_Strumming____Abhijeet(request):
	text = chord.objects.filter(id__iexact =488)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Papon___Pakhi_Pakhi_Guitar_Chords_With_Strumming_Pattern___Abhijeet(request):
	text = chord.objects.filter(id__iexact =489)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Baaghi_2___O_Saathi_Chords_With_Capo__Guitar____Atif_Aslam___Abhijeet(request):
	text = chord.objects.filter(id__iexact =490)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Gulabi_Aankhen_Chords_with_Guitar_Strumming_Pattern___Atif_Aslam_R_D_Burman___Abhijeet(request):
	text = chord.objects.filter(id__iexact =491)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sona_Mohapatra___Anhad_Naad_Guitar_Chords_With_Strumming_Pattern___Lal_Pari_Mastani___Abhijeet(request):
	text = chord.objects.filter(id__iexact =492)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sonu_Nigam___Chaahaton_Ke_Saaye_Mein_Guitar_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =493)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Mere_Sapno_Ki_Rani_Guitar_Chords___Kishore_Kumar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =494)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Arjun_Kanungo__Momina_Mustehsan___Aaya_Na_Tu_Chords___Guitar___Abhijeet(request):
	text = chord.objects.filter(id__iexact =495)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tu_Dua_Hai_Guitar_Chords___Tabs__Darshan_Raval___Abhijeet(request):
	text = chord.objects.filter(id__iexact =496)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Guitar_Chords_of_Darasal___Atif_Aslam___Raabta__With_Strumming_Pattern____Abhijeet(request):
	text = chord.objects.filter(id__iexact =497)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Rahul_Vaidya___Keh_Do_Na_Guitar_Chords_with_Strumming_Pattern___Abhijeet(request):
	text = chord.objects.filter(id__iexact =498)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def De_De_Jagah_Guitar_Chords_with_Strumming_Pattern___Parmanu___Abhijeet(request):
	text = chord.objects.filter(id__iexact =499)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Gal_Sun_Jayein_Guitar_Chords___Akhil_Sachdeva__With_Strumming_Pattern____Abhijeet(request):
	text = chord.objects.filter(id__iexact =500)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Pyar_Nai_Karna_Aya_Guitar_Chords___Karan_Juneja___Punjabi__With_Strumming_Pattern____Abhijeet(request):
	text = chord.objects.filter(id__iexact =501)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sare_Karo_Dab_Guitar_Chords___Sonu_Kakkar__Raftaar__With_Strumming_Pattern____Abhijeet(request):
	text = chord.objects.filter(id__iexact =502)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Aa_Jao_Na_Guitar_Chords___Arijit_Singh___Veere_Di_Wedding__With_Strumming_Pattern____Abhijeet(request):
	text = chord.objects.filter(id__iexact =503)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Jitni_Dafa_Guitar_Chords_From_Parmanu_With_Strumming_Pattern___Abhijeet(request):
	text = chord.objects.filter(id__iexact =504)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Meri_Aashiqui_Guitar_Chords___Balraj_With_Strumming_Pattern___Abhijeet(request):
	text = chord.objects.filter(id__iexact =505)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ghar_Se_Nikalte_Hi_Guitar_Chords___Armaan_Malik___Abhijeet(request):
	text = chord.objects.filter(id__iexact =506)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def SANJU___Main_Badhiya_Tu_Bhi_Badhiya_Guitar_Chords_With_Strumming_Pattern___Abhijeet(request):
	text = chord.objects.filter(id__iexact =507)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Harsohena___Tere_Bin_Guitar_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =508)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Andra___Sudamericana_Guitar_Chords_With_Strumming_Pattern___Abhijeet(request):
	text = chord.objects.filter(id__iexact =509)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ae_Watan_Guitar_Chords___Arijit_Singh___Raazi__With_Strumming____Abhijeet(request):
	text = chord.objects.filter(id__iexact =510)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Selfish_Guitar_Chords___Atif_Aslam___Race_3__With_Strumming_Pattern____Abhijeet(request):
	text = chord.objects.filter(id__iexact =511)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Heeriye_Guitar_Chords_with_Intro_Tabs___Race_3___Abhijeet(request):
	text = chord.objects.filter(id__iexact =512)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tera_Ghata_Guitar_Chords___Gajendra_Verma__With_Strumming_Pattern____Abhijeet(request):
	text = chord.objects.filter(id__iexact =513)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Humnava_Mere_Guitar_Chords___Jubin_Nautiyal__With_Strumming_Pattern____Abhijeet(request):
	text = chord.objects.filter(id__iexact =514)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Dil_Diyan_Gallan_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = chord.objects.filter(id__iexact =515)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Aaj_Se_Teri_Guitar_Chords___Strumming_Pattern___Padman(request):
	text = chord.objects.filter(id__iexact =516)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sanu_Ek_Pal_Chain_Guitar_Chords___Strumming_Pattern___Raid(request):
	text = chord.objects.filter(id__iexact =517)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Lae_Dooba_Guitar_Chords___Strumming_Pattern___Aiyaary(request):
	text = chord.objects.filter(id__iexact =518)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def O_Saathi_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = chord.objects.filter(id__iexact =519)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tera_Yaar_Hoon_Main_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = chord.objects.filter(id__iexact =520)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Gazab_Ka_Hai_Din_Guitar_Chords___Strumming_Pattern___Dil_Juunglee(request):
	text = chord.objects.filter(id__iexact =521)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Lo_Safar_Guitar_Chords___Strumming_Pattern___Baaghi_2(request):
	text = chord.objects.filter(id__iexact =522)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Meri_Khamoshi_Hai_Guitar_Chords___Strumming_Pattern___Pari(request):
	text = chord.objects.filter(id__iexact =523)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Theher_Ja_Guitar_Chords___Strumming_Pattern___October(request):
	text = chord.objects.filter(id__iexact =524)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Boond_Boond_Guitar_Chords___Strumming_Pattern___Hate_Story_4(request):
	text = chord.objects.filter(id__iexact =525)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ye_Ishq_Hai_Guitar_Chords___Strumming_Pattern___Rangoon___Arijit_Singh(request):
	text = chord.objects.filter(id__iexact =526)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tere_Dil_Mein_Guitar_Chords___Strumming_Pattern___Armaan_Malik(request):
	text = chord.objects.filter(id__iexact =527)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def _Most_Romantic_Bollywood_Songs_Guitar_Chords_For_Valentine_Week(request):
	text = chord.objects.filter(id__iexact =528)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kho_Diya_Guitar_Chords___Strumming_Pattern___Bhoomi(request):
	text = chord.objects.filter(id__iexact =529)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tere_Bina_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = chord.objects.filter(id__iexact =530)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Humsafar_Guitar_Chords___Strumming_Pattern___badrinath_ki_dulhania(request):
	text = chord.objects.filter(id__iexact =531)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Meet_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = chord.objects.filter(id__iexact =532)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Hawayein_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = chord.objects.filter(id__iexact =533)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ghar_Guitar_Chords___Strumming_Pattern___Jab_Harry_Met_Sejal(request):
	text = chord.objects.filter(id__iexact =534)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tere_Mere_Darmiyaan_Guitar_Chords___Strumming_Pattern___Chef(request):
	text = chord.objects.filter(id__iexact =535)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Jaane_de_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = chord.objects.filter(id__iexact =536)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Love_You_Zindagi_Guitar_Chords___Strumming_Pattern___Dear_Zindagi(request):
	text = chord.objects.filter(id__iexact =537)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Channa_Mereya_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = chord.objects.filter(id__iexact =538)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def The_Humma_Song_Guitar_Chords___Strumming_Pattern___OK_Jaanu(request):
	text = chord.objects.filter(id__iexact =539)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tu_Hi_Hai_Guitar_Chords___Strumming_Pattern___Dear_Zindagi(request):
	text = chord.objects.filter(id__iexact =540)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Nashe_Si_Chadh_Gayi_Guitar_Chords___Strumming_Pattern___Befikre(request):
	text = chord.objects.filter(id__iexact =541)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Enna_Sona_Guitar_Chords___Strumming_Pattern___OK_Jaanu(request):
	text = chord.objects.filter(id__iexact =542)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Zaalima_Guitar_Chords___Strumming_Pattern___Raees(request):
	text = chord.objects.filter(id__iexact =543)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Pehli_Dafa_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = chord.objects.filter(id__iexact =544)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Bawara_Mann_Guitar_Chords___Strumming_Pattern___Jolly_LLB_2(request):
	text = chord.objects.filter(id__iexact =545)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Orrey_Mon_Guitar_Chords___Strumming_Pattern___Ayushmann_Khurrana(request):
	text = chord.objects.filter(id__iexact =546)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Bulleya_Guitar_Chords___Strumming_Pattern___Ae_Dil_Hai_Mushkil(request):
	text = chord.objects.filter(id__iexact =547)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kaabil_Hoon_Guitar_Chords___Strumming_Pattern___Kaabil(request):
	text = chord.objects.filter(id__iexact =548)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Dariya_Guitar_Chords___Strumming_Pattern___Baar_Baar_Dekho(request):
	text = chord.objects.filter(id__iexact =549)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Dhal_Jaun_Main_Guitar_Chords___Strumming_Pattern___Rustom(request):
	text = chord.objects.filter(id__iexact =550)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Darkhaast_Guitar_Chords___Strumming_Pattern___Shivaay(request):
	text = chord.objects.filter(id__iexact =551)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Toota_Jo_Kabhi_Tara_Guitar_Chords___Strumming___Atif_Aslam(request):
	text = chord.objects.filter(id__iexact =552)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kho_Gaye_Hum_Kahan_Guitar_Chords___Strumming___Baar_Baar_Dekho(request):
	text = chord.objects.filter(id__iexact =553)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Besabriyaan_Guitar_chords___Strumming_Pattern___M_S_Dhoni(request):
	text = chord.objects.filter(id__iexact =554)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ae_Dil_Hai_Mushkil_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = chord.objects.filter(id__iexact =555)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sau_Aasmaan_Guitar_Chords___Strumming_Pattern___Baar_Baar_Dekho(request):
	text = chord.objects.filter(id__iexact =556)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Raaz_Aankhein_Teri_Guitar_Chords___Strumming_Pattern___Raaz_Reboot(request):
	text = chord.objects.filter(id__iexact =557)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Yaad_Hai_Na_Guitar_Chords___Strumming_Pattern___Raaz_Reboot(request):
	text = chord.objects.filter(id__iexact =558)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Phir_Kabhi_Guitar_Chords___Strumming_Pattern___M_S_Dhoni(request):
	text = chord.objects.filter(id__iexact =559)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Jaago_Guitar_chords___Strumming_Pattern___Rock_on_2(request):
	text = chord.objects.filter(id__iexact =560)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Aadat_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = chord.objects.filter(id__iexact =561)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Zara_Si_Dosti_Guitar_Chords___Strumming_Pattern___Happy_Bhag_Jayegi(request):
	text = chord.objects.filter(id__iexact =562)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kuch_Toh_Hai_Guitar_Chords___Strumming_Pattern___Do_Lafzon_Ki_Kahani(request):
	text = chord.objects.filter(id__iexact =563)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Mujhko_Barsaat_Bana_Lo_Guitar_Chords___Strumming_Pattern___Junooniyat(request):
	text = chord.objects.filter(id__iexact =564)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Pani_Da_Rang_Guitar_Chords___Strumming_Pattern___Vicky_Donor(request):
	text = chord.objects.filter(id__iexact =565)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tu_Alvida_Guitar_Chords___Strumming_Pattern___Traffic(request):
	text = chord.objects.filter(id__iexact =566)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ishqe_Di_Lat_Guitar_Chords___Strumming_Pattern___Junooniyat(request):
	text = chord.objects.filter(id__iexact =567)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ikk_Kudi_Guitar_Chords___Strumming_Pattern___Udta_Punjab(request):
	text = chord.objects.filter(id__iexact =568)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Mile_Ho_Tum_Humko_Guitar_Chords___Strumming_Pattern___Fever(request):
	text = chord.objects.filter(id__iexact =569)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Teri_Yaad_Guitar_Chords___Strumming_Pattern___Fever(request):
	text = chord.objects.filter(id__iexact =570)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tere_Sang_Yaara_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = chord.objects.filter(id__iexact =571)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Dekha_Hazaro_Dafaa_Guitar_Chords___Strumming_Pattern___Rustom(request):
	text = chord.objects.filter(id__iexact =572)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Le_Chala_Guitar_Chords___Strumming_Pattern___One_Night_Stand(request):
	text = chord.objects.filter(id__iexact =573)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ijazat_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = chord.objects.filter(id__iexact =574)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Awargi_Guitar_Chords___Strumming_Pattern___Love_Games(request):
	text = chord.objects.filter(id__iexact =575)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Itni_Si_Baat_Hai_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = chord.objects.filter(id__iexact =576)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Bol_Do_Na_Zara_Guitar_Chords___Strumming_Pattern___Azhar(request):
	text = chord.objects.filter(id__iexact =577)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Girl_I_Need_You_Guitar_Chords___Strumming_Pattern___Baaghi(request):
	text = chord.objects.filter(id__iexact =578)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Aafreen_Guitar_Chords___Strumming_Pattern___1920_London(request):
	text = chord.objects.filter(id__iexact =579)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Rootha_Kyun_Guitar_Chords___Strumming_Pattern___1920_London(request):
	text = chord.objects.filter(id__iexact =580)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Pehli_Nazar_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = chord.objects.filter(id__iexact =581)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Salamat_Guitar_Chords___Strumming_Pattern___Sarbjit(request):
	text = chord.objects.filter(id__iexact =582)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Pehla_Nasha_Guitar_Chords___Strumming_Pattern___Amir_Khan(request):
	text = chord.objects.filter(id__iexact =583)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Zara_Sa_Guitar_Chords___Strumming_Pattern___Jannat(request):
	text = chord.objects.filter(id__iexact =584)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Main_Woh_Chaand_Guitar_Chords___Strumming___Teraa_Surroor(request):
	text = chord.objects.filter(id__iexact =585)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tera_Chehra_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = chord.objects.filter(id__iexact =586)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Manwa_Behrupiya_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = chord.objects.filter(id__iexact =587)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Bolna_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = chord.objects.filter(id__iexact =588)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Bekhudi_Guitar_Chords___Strumming_Pattern___Teraa_Surroor(request):
	text = chord.objects.filter(id__iexact =589)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tu_Mere_Paas_Guitar_Chords___Strumming_Pattern___Wazir(request):
	text = chord.objects.filter(id__iexact =590)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Gazab_Ka_Hai_Ye_Din_Guitar_Chords___Strumming_Pattern___Sanam_Re(request):
	text = chord.objects.filter(id__iexact =591)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Rehnuma_Guitar_Chords___Strumming_Pattern___Rocky_Handsome(request):
	text = chord.objects.filter(id__iexact =592)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ji_Huzoori_Guitar_Chords___Strumming_pattern___Ki_And_Ka(request):
	text = chord.objects.filter(id__iexact =593)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sab_Tera_Guitar_Chords___Strumming_Pattern___Baaghi(request):
	text = chord.objects.filter(id__iexact =594)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Wafa_Ne_Bewafai_Guitar_Chords___Strumming_Pattern___Teraa_Surroor(request):
	text = chord.objects.filter(id__iexact =595)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Agar_Tu_Hota_Guitar_Chords___Strumming_Pattern___Baaghi(request):
	text = chord.objects.filter(id__iexact =596)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Soch_Na_Sake_Guitar_Chords___Strumming_Pattern___Airlift(request):
	text = chord.objects.filter(id__iexact =597)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tumhe_Apna_Banane_ka_Junoon_Guitar_Chords___Strumming_Pattern___Hate_Story_3(request):
	text = chord.objects.filter(id__iexact =598)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Gerua_Guitar_Chords___Strumming_Pattern___Dilwale(request):
	text = chord.objects.filter(id__iexact =599)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Safarnama_Guitar_Chords___Strumming_Pattern___Tamasha(request):
	text = chord.objects.filter(id__iexact =600)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Mar_Jaayen_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = chord.objects.filter(id__iexact =601)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Janam_Janam_Guitar_Chords___Strumming_Pattern___Dilwale(request):
	text = chord.objects.filter(id__iexact =602)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sathia_Guitar_Chords___Strumming_Pattern___Ankit_Tiwari(request):
	text = chord.objects.filter(id__iexact =603)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Yeh_Fitoor_Mera_Guitar_Chords___Strumming_Pattern___Fitoor(request):
	text = chord.objects.filter(id__iexact =604)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sanam_Re_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = chord.objects.filter(id__iexact =605)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Atrangi_Yaari_Guitar_Chords___Strumming_Pattern___Wazir(request):
	text = chord.objects.filter(id__iexact =606)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Bandeya_Guitar_Chords___Strumming_Pattern___Jazbaa(request):
	text = chord.objects.filter(id__iexact =607)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Nazdeekiyan_Guitar_Chords___Strumming_Pattern___Shaandaar(request):
	text = chord.objects.filter(id__iexact =608)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Woh_Dekhne_Me_Guitar_Chords___Strumming_Pattern___Ali_Zafar(request):
	text = chord.objects.filter(id__iexact =609)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Lukka_Chuppi_Guitar_Chords___Strumming_Pattern___Rang_De_Basanti(request):
	text = chord.objects.filter(id__iexact =610)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Zara_Zara_Guitar_Chords___Strumming_Pattern___RHTDM(request):
	text = chord.objects.filter(id__iexact =611)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Moora_Guitar_Chords___Strumming_Pattern___Gangs_Of_Wasseypur_2(request):
	text = chord.objects.filter(id__iexact =612)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Awari_Guitar_Chords___Strumming_Pattern___Ek_Villain(request):
	text = chord.objects.filter(id__iexact =613)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Iss_Qadar_Pyar_Hai_Guitar_Chords___Strumming_Pattern___Bhaag_Johnny(request):
	text = chord.objects.filter(id__iexact =614)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Be_Intehaan_Guitar_Chords___Strumming_Pattern___Race_2(request):
	text = chord.objects.filter(id__iexact =615)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Khoya_Khoya_Guitar_Chords___Strumming_Pattern___Hero(request):
	text = chord.objects.filter(id__iexact =616)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sau_Aasoon_Guitar_Chords___Strumming_Pattern___Katti_Batti(request):
	text = chord.objects.filter(id__iexact =617)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def _Rock__Khwaishein_Guitar_Chords___Strumming_Pattern___Calender_Girls(request):
	text = chord.objects.filter(id__iexact =618)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Khwaishein_Guitar_Chords___Strumming_Pattern___Calender_Girls(request):
	text = chord.objects.filter(id__iexact =619)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Woh_Lamhe_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = chord.objects.filter(id__iexact =620)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Roobaroo_Guitar_Chords___Strumming_Pattern___Rang_De_Basanti(request):
	text = chord.objects.filter(id__iexact =621)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Hona_Tha_Pyar_Guitar_chords___Strumming_Pattern___Atif_Aslam(request):
	text = chord.objects.filter(id__iexact =622)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Bhaag_Dk_Bose_Guitar_Chords___Strumming_Pattern___Delhi_Belly(request):
	text = chord.objects.filter(id__iexact =623)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Chal_Chale_Apne_Ghar_Guitar_Chords___Strumming_Pattern___Woh_Lamhe(request):
	text = chord.objects.filter(id__iexact =624)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Hai_Koi_Guitar_Chords___Strumming_Pattern___Gajendra_Verma(request):
	text = chord.objects.filter(id__iexact =625)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Phoolon_Ka_Taaro_Ka_Guitar_Chords___Strumming_Pattern___Raksha_Bandhan(request):
	text = chord.objects.filter(id__iexact =626)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Yaaron_Dosti_Guitar_Chords___Strumming_Pattern___Kk(request):
	text = chord.objects.filter(id__iexact =627)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tu_Jo_Mila_Guitar_Chords___Strumming_Pattern___Bajrangi_Bhaijaan(request):
	text = chord.objects.filter(id__iexact =628)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Zehnaseeb_Guitar_Chords___Strumming_Pattern___Hasee_Toh_Phasee(request):
	text = chord.objects.filter(id__iexact =629)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tu_Na_Jaane_Aas_Pass_Hai_Khuda_Guitar_Chords___Strumming_Pattern(request):
	text = chord.objects.filter(id__iexact =630)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Main_Hoon_Hero_Tera_Guitar_Chords___Strumming_Pattern___Hero(request):
	text = chord.objects.filter(id__iexact =631)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ove_Janiya_Guitar_Chords___Strumming_Pattern___Katti_Batti(request):
	text = chord.objects.filter(id__iexact =632)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Banjarey_Guitar_Chords___Strumming_Pattern_By_Honey_Singh___Fugly(request):
	text = chord.objects.filter(id__iexact =633)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Teri_Galliyan_Guitar_Chords___Strumming_Pattern___Ek_Villian(request):
	text = chord.objects.filter(id__iexact =634)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tum_Hi_Ho_Guitar_Chords___Strumming_Pattern_By_Arijit_Singh___Aashiqui_2(request):
	text = chord.objects.filter(id__iexact =635)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ilahi_Guitar_Chords___Strumming_Pattern_by_Arijit_Singh___Yeh_Jawaani_Hai_Deewani(request):
	text = chord.objects.filter(id__iexact =636)
	lists = chord.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Pehli_Baar_Guitar_Chords___Strumming_Pattern___Dil_Dhadakne_Do(request):
	text = chord.objects.filter(id__iexact =637)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ambarsariya_Guitar_Chords___Strumming_Pattern___Fukrey(request):
	text = chord.objects.filter(id__iexact =638)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tum_Ho_Toh_Guitar_Chords___Strumming_Pattern___Rock_On(request):
	text = chord.objects.filter(id__iexact =639)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Pichle_Saat_Dino_Me_Guitar_Chords___Strumming_Pattern___Rock_On(request):
	text = chord.objects.filter(id__iexact =640)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Saware_Guitar_Chords___Strumming_Pattern_By_Arijit_Singh___Phantom(request):
	text = chord.objects.filter(id__iexact =641)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Give_Me_Some_Sunshine_Guitar_Chords___Strumming_Pattern__3_Idiots(request):
	text = chord.objects.filter(id__iexact =642)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kabira_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = chord.objects.filter(id__iexact =643)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tu_Chahiye_Guitar_Chords___Strumming_Pattern___Bajrangi_Bhaijaan(request):
	text = chord.objects.filter(id__iexact =644)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Jhoom_Guitar_Chords__Strumming_Pattern___Ali_Zafar(request):
	text = chord.objects.filter(id__iexact =645)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Hamari_Adhuri_Kahani_Guitar_Chords___Arijit_Singh(request):
	text = chord.objects.filter(id__iexact =646)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Hasi_Ban_Gaye_Guitar_Chords___Hamari_Adhuri_Kahani(request):
	text = chord.objects.filter(id__iexact =647)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Gulabi_Aankhen_Atif_Aslam_Guitar_Chords___Strumming_Pattern(request):
	text = chord.objects.filter(id__iexact =648)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Jeena_Jeena_Guitar_Chords___Atif_Aslam_Badlapur(request):
	text = chord.objects.filter(id__iexact =649)
	lists = chord.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kuch_Bhi_Karlo_Guitar_Chords___Swastik_the_Band(request):
	text = chord.objects.filter(id__iexact =650)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Chal_Chale_Apne_Ghar_Guitar_Chords___Strumming_Pattern___Woh_Lamhe(request):
	text = chord.objects.filter(id__iexact =651)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Dekha_Hazaro_Dafaa_Guitar_Chords___Strumming_Pattern___Rustom(request):
	text = chord.objects.filter(id__iexact =652)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Bolna_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = chord.objects.filter(id__iexact =653)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Soch_Na_Sake_Guitar_Chords___Strumming_Pattern___Airlift(request):
	text = chord.objects.filter(id__iexact =654)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Main_Rahoon_Ya_Na_Rahoon_Guitar_Chords___Emraan_Hashmi(request):
	text = chord.objects.filter(id__iexact =655)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tumhe_Apna_Banane_ka_Junoon_Guitar_Chords___Strumming_Pattern___Hate_Story_3(request):
	text = chord.objects.filter(id__iexact =656)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Zara_Sa_Guitar_Chords___Strumming_Pattern___Jannat(request):
	text = chord.objects.filter(id__iexact =657)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Iss_Qadar_Pyar_Hai_Guitar_Chords___Strumming_Pattern___Bhaag_Johnny(request):
	text = chord.objects.filter(id__iexact =658)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Main_Hoon_Hero_Tera_Guitar_Chords___Strumming_Pattern___Hero(request):
	text = chord.objects.filter(id__iexact =659)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tere_Sang_Yaara_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = chord.objects.filter(id__iexact =660)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Tum_Hi_Ho_Guitar_Chords___Strumming_Pattern_By_Arijit_Singh___Aashiqui_2(request):
	text = chord.objects.filter(id__iexact =661)
	lists = chord.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Jeena_Jeena_Guitar_Chords___Atif_Aslam_Badlapur(request):
	text = chord.objects.filter(id__iexact =662)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Zehnaseeb_Guitar_Chords___Strumming_Pattern___Hasee_Toh_Phasee(request):
	text = chord.objects.filter(id__iexact =663)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Jhoom_Guitar_Chords__Strumming_Pattern___Ali_Zafar(request):
	text = chord.objects.filter(id__iexact =664)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Be_Intehaan_Guitar_Chords___Strumming_Pattern___Race_2(request):
	text = chord.objects.filter(id__iexact =665)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Teri_Meri_Kahani_Guitar_Chords___Strumming_Pattern___BB_Ki_Vines(request):
	text = chord.objects.filter(id__iexact =666)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Phir_Kabhi_Guitar_Chords___Strumming_Pattern___M_S_Dhoni(request):
	text = chord.objects.filter(id__iexact =667)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Pehli_Nazar_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = chord.objects.filter(id__iexact =668)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Darkhaast_Guitar_Chords___Strumming_Pattern___Shivaay(request):
	text = chord.objects.filter(id__iexact =669)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Kho_Diya_Guitar_Chords___Strumming_Pattern___Bhoomi(request):
	text = chord.objects.filter(id__iexact =670)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Meet_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = chord.objects.filter(id__iexact =671)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Humsafar_Guitar_Chords___Strumming_Pattern___badrinath_ki_dulhania(request):
	text = chord.objects.filter(id__iexact =672)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Sang_Hoon_Tere_Guitar_Chords___Strumming_Pattern___Bhuvan_Bam(request):
	text = chord.objects.filter(id__iexact =673)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Hawayein_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = chord.objects.filter(id__iexact =674)
	lists = chord.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Dil_Diyan_Gallan_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = chord.objects.filter(id__iexact =675)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Aaj_Se_Teri_Guitar_Chords___Strumming_Pattern___Padman(request):
	text = chord.objects.filter(id__iexact =676)
	lists = chord.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Vance_Joy___Riptide_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =677)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Judy_Garland___Somewhere_Over_The_Rainbow___Abhijeet(request):
	text = chord.objects.filter(id__iexact =678)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def John_Legend___All_Of_Me_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =679)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Lukas_Graham___7_Years_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =680)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ruth_B___Lost_Boy_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =681)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def The_Chainsmokers___Closer_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =682)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Plain_White_Ts___Hey_There_Delilah_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =683)
	lists = chord.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Justin_Bieber___Love_Yourself_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =684)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Simon_And_Garfunkel___The_Sound_Of_Silence_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =685)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Oasis___Wonderwall_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =686)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Jason_Mraz___Im_Yours_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =687)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def James_Bay___Let_It_Go_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =688)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Hillsong_United___Oceans_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =689)
	lists = chord.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ed_Sheeran___Thinking_Out_Loud_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =690)
	lists = chord.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Bon_Iver___Skinny_Love_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =691)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Beatles___Hey_Jude_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =692)
	lists = chord.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Adele___Someone_Like_You_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =693)
	lists = chord.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Eagles___Hotel_California_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =694)
	lists = chord.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Jeff_Buckley___Hallelujah_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =695)
	lists = chord.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)

def Ed_Sheeran___Photograph_Chords___Abhijeet(request):
	text = chord.objects.filter(id__iexact =696)
	lists = chord.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/song.html',context)



def Tumhe_Apna_Banane_Ka_Guitar_Tabs___Lead___Hate_Story_3___Abhijeet(request):
    text = chord.objects.filter(id__iexact =1)
    lists = chord.objects.filter(song_names__icontains='n')[:10]
    context={'songs' : text,'lists':lists}
    return render(request,'music/song.html',context)

def theres(request):
    lists = chord.objects.filter(song_names__icontains='love')[:10]
    context={'lists':lists}
    return render(request,'guitar/theres.html',context)

def janiye(request):
    lists = chord.objects.filter(song_names__icontains='love')[:10]
    context={'lists':lists}
    return render(request,'guitar/janiye.html',context)


def sleep(request):
    lists = chord.objects.filter(song_names__icontains='hum')[:10]
    context={'lists':lists}
    return render(request,'guitar/sleep.html',context)


def pal(request):
    lists = chord.objects.filter(song_names__icontains='tum')[:10]
    context={'lists':lists}
    return render(request,'guitar/pal.html',context)


def yaad(request):
    lists = chord.objects.filter(song_names__icontains='piya')[:10]
    context={'lists':lists}
    return render(request,'guitar/yaad.html',context)




def subscribe(request):
    	
		if request.method == 'POST':
    		
			email = request.POST['email']
			print(email)
			sub = email_subscriptions(emails=email)
			try:
				sub.save()
				return render(request,'guitar/guitar.html')
				
			except:
				 return render(request,'guitar/guitar.html')
		
		return render(request,'guitar/guitar.html')
	


def faslo(request):
    
	text = chord.objects.filter(id__iexact =702)
	lists = chord.objects.filter(song_names__icontains='piya')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/guitarall.html',context)


def boot(request):
    
	text = chord.objects.filter(id__iexact =703)
	lists = chord.objects.filter(song_names__icontains='piya')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/guitarall.html',context)



def yeh_dooriya(request):
    	
	text = chord.objects.filter(id__iexact =704)
	lists = chord.objects.filter(song_names__icontains='piya')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/guitarall.html',context)

def shayad(request):
    
	text = chord.objects.filter(id__iexact =705)
	lists = chord.objects.filter(song_names__icontains='piya')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/guitarall.html',context)








