from django.shortcuts import render
from .models import Sargams

def music(request):
    listings =Sargams.objects.filter(song_names__icontains='s')[:80]
    return render(request,'music/main.html',{'listings':listings})

def song(request):
    
    return render(request,'music/bekhayali.html')



def search(request):

     if request.method == 'POST':
            song = request.POST['search_text']
            
          
            text = Sargams.objects.filter(song_names__icontains=song)[:5]

           
     return render(request,'music/ajax_search.html',{'songs':text})


def song_list(request):
    try:
        if request.method == 'POST':
            song = request.POST.get('query', '')
           
			
            text = Sargams.objects.filter(song_names__icontains =song)[:5]
			
           

            context={
                'listings' : text,
            }
           
        return render(request,'music/main.html',context)
    except:
		
        return render(request,'music/main.html')

def sargam(request):
    	return render(request,'music/sargam.html')

def guitar(request):
    	return render(request,'music/guitar.html')


def Teri_Deewani_Kailash_Kher_Harmonium_Sargam_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =1)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bahut_Pyaar_Karte_Hain_Tumko_Sanam_Notes_Sargam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =2)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bahut_Pyar_Karte_Hain_Tumko_Sanam_Harmonium_Sargam__Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =3)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bahut_Pyar_Karte_Hain_Piano_Notes___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =4)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Itna_Na_Mujhse_Tu_Pyar_Badha_Piano_Notes_in_Hindi__Harmonium_Sargam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =5)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Teri_Deewani_Kailash_Kher_Piano_Notes_in_CDF_Notations___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =6)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aye_Mere_Humsafar_Ek_Zara_Intezaar_Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =7)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aaye_Ho_Meri_Zindagi_Mein__Raja_Hindustani__Notes_Sargam_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =8)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Didi_Tera_Devar_Deewana_Sargam__Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =9)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Phoolon_Sa_Chehera_Tera_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =10)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Darde_Dil_Darde_Jigar__Karz__Piano_Notes_in_Hindi__Harmonium_Sargam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =11)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Moh_Moh_Ke_Dhaage_Song_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =12)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kajra_Mohabbat_Wala_Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =14)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Ke_Jharoke_Mein_Piano_Notes_in_Hindi__Harmonium_Sargam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =15)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Mehboob_Qayamat_Hogi_Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =17)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Abhi_Mujh_Mein_Kahin__Sonu_Nigam__Harmonium_Notes__Sargam_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =19)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Janam_Janam__Arijit_Singh__Piano_Notes__Notations_in_English___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =20)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Abhi_Mujh_Mein_Kahin_Piano_Notes_in_CDF_Notations___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =22)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hum_Tere_Shahar_Mein_Aaye_Hain__Ghazal__Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =23)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mera_Piya_Ghar_Aaya_Song_Harmonium_Notes__Sargam_in_Hindi__Piano____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =24)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Lag_Jaa_Gale_Song_Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =25)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Sapno_Ki_Rani_Kab_Aayegi_Tu_Harmonium_Sagam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =26)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Saat_Samundar_Paar_Main_Tere_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =27)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Teri_Mitti__Kesari__Song_Harmonium_Sargam__Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =28)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kaun_Tujhe__MS_Dhoni__Harmonium_Sargam_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =29)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tumhe_Dillagi_Bhool_Jani_Padegi_Harmonium_Sargam__Piano_Notes_in_Hindi____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =30)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kaun_Tujhe__MS_Dhoni__Piano_Notes__Notations_with_Lyrics___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =31)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Likhe_Jo_Khat_Tujhe_Harmonium_Sargam___Piano_Notes___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =34)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Baharon_Phool_Barsao_Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =35)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pehla_Nasha_Pehla_Khumar_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =37)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Zindagi_Ek_Safar_Hai_Suhana_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =38)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ghar_Aaya_Mera_Pardesi_Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =39)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Apna_Aur_Preet_Parai_Song_Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =40)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Apni_to_Jaise_Taise_Song_Piano_Notes__Notations____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =41)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Neele_Neele_Ambar_Par_song_Piano_Notes_in_Hindi__Harmonium_Sargam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =43)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sandese_Aate_Hain_Piano_Notes_in_Sa_re_ga_ma___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =45)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ajeeb_Dastan_Hai_Yeh_Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =46)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Saamne_Wale_Khidki_Song_Sargam__Notations_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =47)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Phoolon_Sa_Chehra_Tera_Song_Piano_Notes__CDF_Notations___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =49)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Teri_Hai_Zameen_Tera_Aasman_Harmonium_Notes___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =52)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Cheez_Badi_Hai_Mast_Mast_Sargam__Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =53)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Shayar_To_Nahin_Harmoinim_Notes__Sargam_in_Hindi_for_Piano___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =55)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Rashke_Qamar__Baadshaho__Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =59)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Apni_To_Jaise_Taise__Housefull__O_Dhanno_Sargam_Notes_for_Harmonium_Piano___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =60)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ek_Pardesi_Mera_Dil_Le_Gaya_Harmonium_Sargam__Piano_Notes___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =61)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Ke_Armaan_Aansuon_Mein_Beh_Gaye_Notes_Sargam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =62)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Rashke_Qamar_Piano_Keyboard_Notations__CDF_Notes____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =63)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sanam_Re_Full_Song_Piano_Notes__Line_by_Line_By_Notations_with_Lyrics___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =67)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Yeh_Shaam_Mastani_Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =68)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gulabi_Aankhein_Jo_Teri_Dekhi_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =70)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ye_Reshmi_Zulfein_Ye_Sharbati_Aankhein_Notes_Sargam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =72)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Karvaten_Badalte_Rahe_Sari_Raat_Hum_Sargam__Harmonium_Notes_in_Hindi____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =75)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Do_Lafzon_Ki_Hai_Dil_Ki_Kahani_Sargam_Notes___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =78)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Zindagi_Pyar_Ka_Geet_Hai_Sargam_Harmonium__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =79)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Teri_Mitti__Kesari__Piano_Notes__Western_Notations___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =81)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bahon_Mein_Chale_Aao_Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =85)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_Bina_Zindagi_Se_Koi_Shikwa_Notes_in_Hindi__Sargam__Piano_Notations___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =87)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Hai_Ke_Manta_Nahi_Harmonium_Notes__Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =93)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aaj_Purani_Raahon_Se_Koi_Mujhe__Song__Harmonium_Sargam__Notes_Piano___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =94)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Lootne_Wale_Jadugar_Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =95)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Milti_Hai_Zindagi_Mein_Mohabbat_Kabhi_Kabhi_Harmonium_Notes_Notations_Sargam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =96)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kaun_Disa_Mein_Leke_Piano_Notes_in_Hindi__Harmonium_Sargam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =97)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Naseeb_Mein_Tu_Hai_Ke_Nahin_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =99)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kabhi_Ram_Banke_Kabhi_Shyam_Banke_Bhajan_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =103)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hey_Ram_Hey_Ram_Bhajan_Sargam_for_Harmonium__Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =104)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mile_Ho_Tum_Humko_Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =106)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aane_Se_Uske_Aaye_Bahar_Notes_Sargam_in_Hindi_for_Harmonium_and_Piano___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =111)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Zindagi_Ki_Na_Toote_Ladi_Harmonium_Sargam__Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =113)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Teri_Dushman_Song_Piano_Notes_in_Hindi__Harmonium_Sargam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =115)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sanwali_Surat_Pe_Mohan_Dil_Deewana_Hogya_Sargam_Notes___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =121)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ghanshyam_Teri_Bansi_Harmonium_Sargam__Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =122)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pal_Pal_Dil_Ke_Paas_Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =123)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kala_Kala_Kahe_Gujri_Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =124)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aaarti_Kunj_Bihari_ki_Harmonium_Sargam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =125)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Radhe_Radhe_Japo_Chale_Ayenge_Bihari_Sargam_Harmonium__Piano_Notes___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =126)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Yashomati_Maiya_Se_Bole_Nandlala_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =127)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gaiya_Maiya_Bula_Rahi_Hai_Harmonium_Sargam__Piano_Notes___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =128)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kya_Khoob_Lagti_Ho_Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =131)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hum_Tumhe_Chahte_Hain_Aise_Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =132)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Hi_Re_Song_Piano_Notations__Keyboard_Western_Notes___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =140)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Desh_Ki_Dharti_Notes_for_Piano_and_Harmonium___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =141)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bachpan_Ki_Mohabbat_Ko__Baiju_Bawra__Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =151)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aap_Ki_Nazron_Ne_Smjha_Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =153)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ab_To_Hai_Tumse_Song_Sargam__Piano_Notes_in_Hindi____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =154)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chalte_Chalte_Yunhi_Koi_Sargam__Harmonium_Notes__Piano_Notation___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =156)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Woh_Jab_Yaad_Aaye_Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =162)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Saajan_Mera_Us_Paar_Hai_Sargam_Harmonium__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =164)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ek_Do_Teen__Tezaab__Song_Harmonium_Sargam__Piano_Notes_in_Hindi____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =165)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ek_Do_Teen__Old_Song__Piano_Notes__CDF_Notations_for_Keyboard___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =166)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dheere_Dheere_Se_Meri_Zindagi_Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =174)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pardesi_Pardesi_Jana_Nahi_Notes__Sargam_in_Hindi_for_Harmonium_and_Piano___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =175)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kitna_Haseen_Chehra__Dilwale__Song_Notes__Sargam_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =176)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mera_Dil_Bhi_Kitna_Pagal_Hai_Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =178)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tujhe_Dekha_To_Ye_Jaana_Sanam_Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =179)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ek_Pyar_Ka_Nagma_Hai__Shor__keyboard_Piano_Notations_Notes___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =183)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dheere_Dheere_Se_Meri_Zindagi_Mein_Piano_Keyboard_Notes_in_CDF___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =185)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ek_Pyar_Ka_Nagma_Hai_Harmonium_Notes__Sargam__Sa_Re_Ga_Ma_Notations___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =186)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mile_Ho_Tum_Humko_Piano_Notes_in_English__CDF_Notations____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =215)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hothon_Se_Chhulo_Tum_Song_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =218)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hai_Apna_Dil_To_Awara_Piano_Notes_in_Hindi__Harmonium_Sargam____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =219)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chupke_Chupke_Raat_Din_Ghulam_Ali_Ghazal_Notes_Sargam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =223)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jana_Gana_Mana_National_Anthem_Harmonium_Notes_Sargam_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =229)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Krishna_Bhajan_Mohan_Se_Dil_Kyun_Lagaya_Hai_Notes_Sargam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =230)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sare_Jahan_Se_Acha_Hindustan_Humara_Harmonium_Notes__Piano_Notations___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =233)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jai_Ganesh_Jai_Ganesh_Jai_Ganesh_Deva_Harmonium_Notes__Sargam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =234)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Om_Jai_Jagdish_Hare_Aarti_Harmonium_Notes__Slow_Tutorial____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =235)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Om_Jai_Jagdish_Hare_Aarti_Harmonium_Piano_Notes_in_Hindi__sargam____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =237)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gayati_Mantra_Piano_Notes_and_Harmonium_Sargam_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =239)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Om_Jai_Jagdish_Hare_Aarti_Piano_Notes_and_Tutorial___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =241)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dar_Chhod_Ke_Jaunga_Na_Maiya_Bhajan_Sargam__Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =245)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_Hi_Ho__Aashqui_2__Sargam__Hindi_Notes_for_Harmonium_Piano___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =250)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Rashke_Qamar_Sargam_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =252)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aa_Jao_Bhole_Baba_Mere_Makan_Mein_Sargam_Harmonium__Piano_Notes___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =256)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hum_Honge_Kamyab_Song_Harmonium_Notations__Sargam_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =258)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aye_Mere_Watan_Ke_Logo_Piano_Harmonium_Notes___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =261)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Vande_Mataram_Song_Notes_for_Piano_and_Harmonium___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =262)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_To_Thehre_Pardesi__Altaf_Raja__Harmonium_Notes__Piano_Notations___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =286)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mann_Dole_Mera_Tann_Dole_Sargam_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =295)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Rang_Barse_Bheege_Chunar_Wali_Harmonium_Notes_Sargam_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =343)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dekhte_Dekhte__Batti_Gul_Meter_Chalu____Sargam_And_Flute_(request):
	text = Sargams.objects.filter(id__iexact =379)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Moh_Moh_ke_dhaage__Dum_Laga_Ke_Haisha____Sargam_And_Flute_(request):
	text = Sargams.objects.filter(id__iexact =380)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Baarish_Lete_Aana__Darshan_Raval____Sargam_And_Flute_(request):
	text = Sargams.objects.filter(id__iexact =381)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Intezaar__Arijit_Singh____Sargam_And_Flute_(request):
	text = Sargams.objects.filter(id__iexact =382)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pal_Pal_Dil_Ke_Paas__Kishore_Kumar____Sargam_And_Flute_(request):
	text = Sargams.objects.filter(id__iexact =383)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Rahoon_Ya_Na_Rahoon__Armaan_Malik____Sargam_And_Flute_(request):
	text = Sargams.objects.filter(id__iexact =384)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Mileya__Darshan_Raval____Sargam_And_Flute_(request):
	text = Sargams.objects.filter(id__iexact =385)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bechara_dil_kya_kare___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =498)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Banjara__Jaise_Banjare_Ko_Ghar____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =499)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bhor_bhaye_panghat_pe___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =500)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bavra_Mann_Dekhne_Chala_Ek_Sapna___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =501)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bahut_Pyar_Karte_Hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =502)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bhigi_bhigi_rato_me___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =503)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bheege_hont_tere___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =504)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bheegi_Bheegi_Si_Hai_Raatein___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =505)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bahut_door_mujhe_chale_jana_hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =506)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bahon_me_chale_aao___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =507)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Baar_baar_din_ye_aye__happy_birthday____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =508)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aye_mere_watan_ke_logo___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =509)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Awarapan__Banjarapan___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =510)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Babuji_dheere_chalna___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =511)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bade_Achhe_lagte_hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =512)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Awaz_deke_hame_tum_bulao___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =513)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Zindagi_mil_ke_bitayenge___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =514)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Zara_zara_mehekta_hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =515)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Zindagi_kaisi_hai_paheli_haye___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =516)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ye_raate_ye_mausam_ye_nadi_ka_kinara___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =517)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ye_raat_ye_chandni_fir_kahan___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =518)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ye_nayan_dare_dare___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =519)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ye_moh_moh_ke_dhaage___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =520)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ye_kya_hua___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =521)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ye_jo_mohabbat_hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =522)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ye_Jawani_Hai_Diwani___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =523)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ye_haseen_Wadiya_Ye_Khula_Asmaan___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =524)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ye_dil_ye_paagal_dil_mera___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =525)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ye_dil_Diwana_hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =526)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ye_Awara_Raatein___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =527)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ye_Jeevan_Hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =528)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Yamma_Yamma___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =529)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Yaadon_Ki_Baraat___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =530)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Wo_shaam_kuchh_ajeeb_thi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =531)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Waqt_ne_kiya___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =532)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Wada_raha_sanam___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =533)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Vande_Mataram__Anand_Math____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =534)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Wada_karo_nahi_chhorogi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =535)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tune_Mere_Jana__Emptiness____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =536)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def tumse_milke_aisa_laga___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =537)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tumhen_yaad_karte_karte___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =538)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tumse_Hi__Na_hai_ye_paana_______Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =539)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tumse_kahoon_ek_baat_paron_se_halki_halki___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =540)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tumane_mujhe_dekha___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =541)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_se_hi_din_hota_hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =542)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_pukar_lo___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =543)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tumhe_apna_banaane_ki_kasam___ka_junoo___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =544)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_Paas_Aaye___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =545)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_itna_jo_muskura_rahe_ho___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =546)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_mile_to_jeena_aa_gaya___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =547)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_Dil_ki_dhadkan_me___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =548)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_bin_jiya_jaye_kaise___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =549)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_bhi_chalo___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =550)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tujhe_dekh_dekh_sona___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =551)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tujhse_naraz_nahi_zindagi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =552)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tujhe_Suraj_Kahu_ya_Chanda___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =553)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_tu_hai_wahi_dil_ne_jise___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =554)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Mile_Dil_Khile___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =555)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Hi_Re___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =556)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Teri_meri_meri_teri___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =557)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_mast_mast_do_nain___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =558)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_liye___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =559)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_bina_zindagi_se___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =560)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Teri_galliyan___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =561)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_bina_jiya_jaye_na___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =562)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_bin_tere_bin___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =563)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_bin_nayi_lagda_dil_mera_dholna___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =564)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tanhayee___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =565)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Surmayee_ankhiyon_me___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =566)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tadap_Tadap_ke_is_dil_se___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =567)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Suno_na_sange_marmar_ki___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =568)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Suno_gaur_sey_duniya_walon___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =569)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sunn_raha_hai_na_tu___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =570)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Solah_baras_ki_bali_umar_ko_salam___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =571)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Shyam_teri_bansi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =572)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Seene_me_jalan___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =573)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sawan_ka_mahina___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =574)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Satyam_Shivam_Sundaram___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =575)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sathiya_tune_kya_kiya___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =576)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Saranga_teri_yaad_me___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =577)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sapne_me_sajan_se_do_batein___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =578)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sanwaar_loon___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =579)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sanam_Re_sanam_re___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =580)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Saiyyan__Heere_Moti_main_na_chahu____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =581)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Roop_tera_mastana___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =582)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Rimjhim_Gire_Sawan___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =583)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Rimjhim_Rimjhim_Rumjhum_Rumjhum___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =584)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Rasik_Balma___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =585)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ranjish_Hi_Sahi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =586)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Rang_Barse_Bhige_Chunar_Wali___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =587)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Raat_Kali_ek_khwaab_mein_aayee___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =588)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pyar_Diwana_Hota_Hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =589)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pukarta_chalaa_hun_mein___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =590)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Puchho_na_kaise_maine_rain_bitai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =591)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Piya_to_se_naina_lage_re___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =592)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Piya_Re_Piya_Re___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =593)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Phoolon_Ka_Taron_Ka___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =594)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pehla_nasha_pehla_khumar___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =595)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pardesiya_ye_sach_hai_piya___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =596)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pankh_Hote_Toh_Udd_Aati_Re___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =597)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pani_da_rang_wekh_ke___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =598)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pal_Pal_Pal___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =599)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pal_pal_dil_ke_paas___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =600)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def O_Sajnaa__barakha_bahaar_aayee___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =601)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def O_ri_chiraiya___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =602)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def O_saathi_re___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =603)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def O_Re_Piya___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =604)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def O_re_manva_tu_kyu_bavra_hai__Iktara____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =605)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def O_majhi_re___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =606)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def O_hansini___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =607)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def O_mere_dil_ke_chain___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =608)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Neele_Gagan_Ke_Tale___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =609)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Neela_asman_so_gaya___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =610)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Nanha_Munna_Rahi_Hu___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =611)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Naino_me_badra_chhaye___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =612)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Naina_Barse_Rim_jhim_Rim_jhim___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =613)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Nahi_Nahi_Abhi_Nahi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =614)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Nadiya_se_Dariya___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =615)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Na_maaye_naa_bhej_mujhe___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =616)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Muthukodi_Kawadi_Hada___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =617)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Musafir_Hu_Yaro___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =618)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mujhko_is_raat_ki_tanhayi_me___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =619)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def More_saiyyan_to_hai_pardes___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =620)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mohabbaten_Lutaungaa___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =621)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mitwa__Mere_man_ye_bata_de_tu____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =622)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Meri_bhigi_bhigi_si___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =623)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_rashk_e_kamar___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =624)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Rang_Mein_rangne_wali___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =625)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Nishaan__OMG____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =626)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_naina_sawan_bhadon___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =627)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_mehboob_qayamat_hogi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =628)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_khwabo_me_jo_aye___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =629)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_hath_mein___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =630)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_dil_me_aj_kya_hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =631)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mera_mulk_mera_desh___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =632)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Megha_chhaye_aadhi_raat___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =633)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Manwa_Lage___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =634)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Man_re_tu_kahe_na_dhir_dhare___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =635)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Man_Mast_Magan___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =636)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_tenu_samjhawa_ki___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =637)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_rahu_ya_na_rahu___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =638)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mai_ye_soch_kar_uske_dar_se___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =639)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Kabhi_Batlata_Nahin__Maa____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =640)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mai_shayar_badnam___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =641)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Madhosh_dil_ki_dhadkan___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =642)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Lukka_chuppi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =643)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Lambi_Judaai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =644)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Laila_main_laila___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =645)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Lag_Ja_Gale___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =646)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kyuki_Tum_Hi_Ho___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =647)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kyu_na_bole_mose_mohan_kyu___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =648)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kya_yehi_pyar_hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =649)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kurbaan_Hua___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =650)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kuhu_Kuhu_bole_koyaliya___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =651)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kora_Kagaz_Tha_Yeh_Mann_Mera___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =652)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Koi_ye_kaise_bataaye___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =653)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Koi_Humdum_Na_Raha___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =654)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kiska_rasta_dekhe___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =655)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Khoya_Khoya_Chand_Khula_Aasman___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =656)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kehna_hai__Kehna_hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =657)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kaun_hai_jo_sapno_me_aya___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =658)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kasme_vade_pyar_wafa_sab___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =659)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kash_tere_ishq_me_nilam_ho_jau___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =660)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kariye_Na_Kariye_Na___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =661)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kal_ho_na_ho__Har_ghadi_badal_rahi_hai_______Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =662)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kahin_Karti_Hogi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =663)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kahin_door_jab_din_dhal_jaye___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =664)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kaha_tak_ye_man_ko___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =665)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kabhi_Sham_Dhale___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =666)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kabhi_kabhi_mere_dil_me___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =667)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ka_Karu_Sajni_Aye_na_baalam___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =668)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jogi_Jab_Se_Yu_Aya_Mere_Dware___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =669)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jeene_Laga_Hoon___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =670)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jeena_Yahan_Merna_Yahan___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =671)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jeena_Jeena___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =672)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jaun_kahan_bata_aye_dil___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =673)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jashn_e_bahara___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =674)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Janeman_Janeman_Tere_Do_Nayan___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =675)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jane_Woh_Kaise_Log_The___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =676)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jane_kyu_log_mohabbat_kiya_karte_ha___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =677)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jane_kya_dhoondti_rehti_hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =678)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jane_Kahan_Gaye_Wo_Din___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =679)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jane_do_na__Paas_aao_na___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =680)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Janam_janam_janam___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =681)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jai_jai_shiv_shankar___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =682)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jab_koi_baat_bigad_jaaye___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =683)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jaane_Kya_Baat_Hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =684)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Itna_na_mujhase_tu_pyar_badha___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =685)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jaane_ja_dhundhta_fir_raha___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =686)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Itni_shakti_hame_dena_daata___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =687)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Isharo_isharo_me_dil_lene_wale___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =688)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ik_hasee_shaam_ko___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =689)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ik_aisi_ladki_thi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =690)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hum_tere_sheher_me_aye_hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =691)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Humma_humma__ik_ho_gaye_hum_aur_tum____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =692)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hum_tere_bin_ab_jee_nahi_sakte__Kyuki_Tum_hi_ho____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =693)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hum_dono_do_premi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =694)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hum_rahe_ya_na_rahe_kal___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =695)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hum_dil_de_chuke_sanam___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =696)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hum_Bewafa_Hargeez_Na_The___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =697)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hum_Aapke_Hain_Kaun___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =698)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hoshwalo_ko_khabar_kya___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =699)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hothon_se_chhoo_lo_tum___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =700)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Har_kisi_ko_nahi_milta__Do_Lafz_ki_hai____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =701)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hame_tumse_pyaar_kitna___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =702)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hamari_Adhuri_Kahani__Title_Song____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =703)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hai_apna_dil_to_awara___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =704)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gumnam_hai_koi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =705)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gulabi_ankhen_jo_teri_dekhi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =706)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ghungroo_ki_tarah___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =707)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ghar_jayegi_tar_jayegi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =708)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ghar_Aaya_Mera_Pardesi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =709)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gerua__Dhoop_se_nikal_ke____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =710)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ek_Ladki_ko_dekha_to___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =711)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ek_daal_par_tota_bole___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =712)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ehsaan_Tera_Hoga_Mujh_Par___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =713)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ek_Ajnabi_Haseena_Se___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =714)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Doraemon_theme_song__Hindi____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =715)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Doston_se_jhooti_mooti___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =716)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Doli_me_bithai_ke_kahar___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =717)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Do_Lafzon_Ki_Hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =718)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_to_bachcha_hai_ji___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =719)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Din_dhal_jaye___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =720)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Se_Re______Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =721)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Smbhal_ja_zara___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =722)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Pukare_Aare_Aare_Aare___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =723)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_ne_kaha_chupke_se___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =724)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_lootne_wale_jadugar___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =725)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Hoom_Hoom_Kare___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =726)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_diydiyan_gallan___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =727)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_hai_chota_sa___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =728)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_diya_hai_jaan_bhi_denge___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =729)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dhadkan_zara_ruk_gayi_hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =730)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dekha_Na_Haay_Re___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =731)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Deewana_hua_baadal___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =732)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dard_dilo_ke_kam_ho_jate___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =733)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chura_liya_hai_tumne_jo___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =734)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chupke_Chupke_Raat_Din___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =735)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chup_chup_khade_ho___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =736)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chori_chori_teri_meri_love_story___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =737)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Choodi_nahi_ye_mera___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =738)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chingari_koyi_bhadake___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =739)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chhupa_Lo_yun_Dil_me___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =740)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chhoo_kar_mere_man_ko___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =741)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chehra_hai_ya_chand_khila___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =742)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chak_Dhoom_Dhoom_____Koi_Ladki_Hai_Jab_Wo_Hasti_Hai____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =743)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chandan_sa_badan___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =744)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chaha_tujhe_hai__Band_of_Boys____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =745)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chaha_Hai_Tujhko___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =746)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Breathless___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =747)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bolna_Mahi_Bolna___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =748)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Apki_ankhon_me_kuchh___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =749)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ankhon_me_teri_ajab_si___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =750)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Albela_sajan_aayo_ree___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =751)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Alvida__alvida___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =752)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Akele_hai_to_kya_gham_hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =753)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aja_re_mai_to_kab_se___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =754)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aj_jane_ki_zid_na_karo___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =755)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aise_na_mujhe_tum_dekho___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =756)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ahatein_ho_rahi_teri__MTV_Splitsvilla____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =757)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ae_Zindagi_Gale_Laga_Le___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =758)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Abhi_naa_jao_chhod_kar___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =759)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Abhi_mujh_mein_kahin___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =760)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aawara_hoon___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =761)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ab_To_Hai_Tumse___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =762)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aate_jate_hanste_gaate___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =763)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aap_ke_haseen_rukh_pe___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =764)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aaoge_jab_tum_o_saajna___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =765)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aao_na_gale_lagalo_na___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =766)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aaja_sanam_madhur_chandni_mein_hum___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =767)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aane_wala_pal_jane_wala_hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =768)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aa_jaane_ja___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =769)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aaja_aaja_mai_hu_pyaar_tera___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =770)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def saajan_mera(request):
	text = Sargams.objects.filter(id__iexact =771)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Theres_Nothing(request):
	lists = Sargams.objects.filter(song_names__icontains='dil')[:10]
	context={'lists':lists}
	return render(request,'music/theres_nothing.html',context)


def wolves(request):
	lists = Sargams.objects.filter(song_names__icontains='hum')[:10]
	context={'lists':lists}
	return render(request,'music/wolves.html',context)

def wheels(request):
	lists = Sargams.objects.filter(song_names__icontains='hum')[:10]
	context={'lists':lists}
	return render(request,'music/wheels.html',context)

def ab_tere(request):
	lists = Sargams.objects.filter(song_names__icontains='tere')[:10]
	context={'lists':lists}
	return render(request,'music/tere.html',context)

def atake(request):
	lists = Sargams.objects.filter(song_names__icontains='tum')[:10]
	context={'lists':lists}
	return render(request,'music/atake.html',context)

def jaja(request):
	lists = Sargams.objects.filter(song_names__icontains='dil')[:10]
	context={'lists':lists}
	return render(request,'music/jaja.html',context)

def shankara(request):
	lists = Sargams.objects.filter(song_names__icontains='yar')[:10]
	context={'lists':lists}
	return render(request,'music/shankara.html',context)

def rangeela(request):
	lists = Sargams.objects.filter(song_names__icontains='hum')[:10]
	context={'lists':lists}
	return render(request,'music/rangeela.html',context)

def bijji(request):
	lists = Sargams.objects.filter(song_names__icontains='mile')[:10]
	context={'lists':lists}
	return render(request,'music/bijji.html',context)

	
def baby(request):
	lists = Sargams.objects.filter(song_names__icontains='deewani')[:10]
	context={'lists':lists}
	return render(request,'music/baby.html',context)


def kabhi_kabhi(request):
    
	text = Sargams.objects.filter(id__iexact =785)
	lists = Sargams.objects.filter(song_names__icontains='kabhi')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/naina.html',context)

def tu_pyar(request):

	text = Sargams.objects.filter(id__iexact =786)
	lists = Sargams.objects.filter(song_names__icontains='tu')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/naina.html',context)

def filhal(request):

	text = Sargams.objects.filter(id__iexact =787)
	lists = Sargams.objects.filter(song_names__icontains='aye')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/naina.html',context)


def mere_naina(request):

	text = Sargams.objects.filter(id__iexact =788)
	lists = Sargams.objects.filter(song_names__icontains='mere')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/naina.html',context)

def tumse_milke(request):

	text = Sargams.objects.filter(id__iexact =789)
	lists = Sargams.objects.filter(song_names__icontains='naina')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/naina.html',context)

def pachtaoge(request):

	text = Sargams.objects.filter(id__iexact =790)
	lists = Sargams.objects.filter(song_names__icontains='naina')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/naina.html',context)

def chale_aana(request):

	text = Sargams.objects.filter(id__iexact =791)
	lists = Sargams.objects.filter(song_names__icontains='chale')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/naina.html',context)
