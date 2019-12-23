def Banjara__Jaise_Banjare_Ko_Ghar_(request):
	text = Sargams.objects.filter(id__iexact =364)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Baar_baar_din_ye_aye__happy_birthday_(request):
	text = Sargams.objects.filter(id__iexact =365)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Bade_Achhe_lagte_hai(request):
	text = Sargams.objects.filter(id__iexact =366)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Aye_mere_watan_ke_logo(request):
	text = Sargams.objects.filter(id__iexact =367)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Bahut_Pyar_Karte_Hai(request):
	text = Sargams.objects.filter(id__iexact =368)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Babuji_dheere_chalna(request):
	text = Sargams.objects.filter(id__iexact =369)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Bahon_me_chale_aao(request):
	text = Sargams.objects.filter(id__iexact =370)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Bahut_door_mujhe_chale_jana_hai(request):
	text = Sargams.objects.filter(id__iexact =371)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Ankhon_me_teri_ajab_si(request):
	text = Sargams.objects.filter(id__iexact =372)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Awarapan__Banjarapan(request):
	text = Sargams.objects.filter(id__iexact =373)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Alvida__alvida(request):
	text = Sargams.objects.filter(id__iexact =374)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Akele_hai_to_kya_gham_hai(request):
	text = Sargams.objects.filter(id__iexact =375)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Aja_re_mai_to_kab_se(request):
	text = Sargams.objects.filter(id__iexact =376)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Apki_ankhon_me_kuchh(request):
	text = Sargams.objects.filter(id__iexact =377)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Albela_sajan_aayo_ree(request):
	text = Sargams.objects.filter(id__iexact =378)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Zindagi_kaisi_hai_paheli_haye(request):
	text = Sargams.objects.filter(id__iexact =379)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Zindagi_mil_ke_bitayenge(request):
	text = Sargams.objects.filter(id__iexact =380)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Zara_zara_mehekta_hai(request):
	text = Sargams.objects.filter(id__iexact =381)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Ye_raate_ye_mausam_ye_nadi_ka_kinara(request):
	text = Sargams.objects.filter(id__iexact =382)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Ye_raat_ye_chandni_fir_kahan(request):
	text = Sargams.objects.filter(id__iexact =383)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Ye_nayan_dare_dare(request):
	text = Sargams.objects.filter(id__iexact =384)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Awaz_deke_hame_tum_bulao(request):
	text = Sargams.objects.filter(id__iexact =385)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Ye_moh_moh_ke_dhaage(request):
	text = Sargams.objects.filter(id__iexact =386)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Ye_kya_hua(request):
	text = Sargams.objects.filter(id__iexact =387)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Ye_jo_mohabbat_hai(request):
	text = Sargams.objects.filter(id__iexact =388)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Ye_Jeevan_Hai(request):
	text = Sargams.objects.filter(id__iexact =389)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Ye_Jawani_Hai_Diwani(request):
	text = Sargams.objects.filter(id__iexact =390)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Ye_dil_ye_paagal_dil_mera(request):
	text = Sargams.objects.filter(id__iexact =391)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Ye_dil_Diwana_hai(request):
	text = Sargams.objects.filter(id__iexact =392)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Ye_Awara_Raatein(request):
	text = Sargams.objects.filter(id__iexact =393)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Yamma_Yamma(request):
	text = Sargams.objects.filter(id__iexact =394)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Yaadon_Ki_Baraat(request):
	text = Sargams.objects.filter(id__iexact =395)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Wo_shaam_kuchh_ajeeb_thi(request):
	text = Sargams.objects.filter(id__iexact =396)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Waqt_ne_kiya(request):
	text = Sargams.objects.filter(id__iexact =397)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Wada_raha_sanam(request):
	text = Sargams.objects.filter(id__iexact =398)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Wada_karo_nahi_chhorogi(request):
	text = Sargams.objects.filter(id__iexact =399)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Tune_Mere_Jana__Emptiness_(request):
	text = Sargams.objects.filter(id__iexact =400)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Vande_Mataram__Anand_Math_(request):
	text = Sargams.objects.filter(id__iexact =401)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_tumse_milke_aisa_laga(request):
	text = Sargams.objects.filter(id__iexact =402)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Tumhen_yaad_karte_karte(request):
	text = Sargams.objects.filter(id__iexact =403)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Tumse_Hi__Na_hai_ye_paana____(request):
	text = Sargams.objects.filter(id__iexact =404)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Tumhe_apna_banaane_ki_kasam___ka_junoo(request):
	text = Sargams.objects.filter(id__iexact =405)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Tumse_kahoon_ek_baat_paron_se_halki_halki(request):
	text = Sargams.objects.filter(id__iexact =406)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Tum_se_hi_din_hota_hai(request):
	text = Sargams.objects.filter(id__iexact =407)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Tum_pukar_lo(request):
	text = Sargams.objects.filter(id__iexact =408)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Tum_Paas_Aaye(request):
	text = Sargams.objects.filter(id__iexact =409)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Tumane_mujhe_dekha(request):
	text = Sargams.objects.filter(id__iexact =410)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Tum_itna_jo_muskura_rahe_ho(request):
	text = Sargams.objects.filter(id__iexact =411)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Tum_mile_to_jeena_aa_gaya(request):
	text = Sargams.objects.filter(id__iexact =412)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Tum_Dil_ki_dhadkan_me(request):
	text = Sargams.objects.filter(id__iexact =413)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Tum_bhi_chalo(request):
	text = Sargams.objects.filter(id__iexact =414)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Tum_bin_jiya_jaye_kaise(request):
	text = Sargams.objects.filter(id__iexact =415)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Tujhse_naraz_nahi_zindagi(request):
	text = Sargams.objects.filter(id__iexact =416)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Tujhe_dekh_dekh_sona(request):
	text = Sargams.objects.filter(id__iexact =417)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Tu_Mile_Dil_Khile(request):
	text = Sargams.objects.filter(id__iexact =418)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Tu_Hi_Re(request):
	text = Sargams.objects.filter(id__iexact =419)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Tujhe_Suraj_Kahu_ya_Chanda(request):
	text = Sargams.objects.filter(id__iexact =420)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Teri_galliyan(request):
	text = Sargams.objects.filter(id__iexact =421)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Teri_meri_meri_teri(request):
	text = Sargams.objects.filter(id__iexact =422)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Tere_mast_mast_do_nain(request):
	text = Sargams.objects.filter(id__iexact =423)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Tere_liye(request):
	text = Sargams.objects.filter(id__iexact =424)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Tere_bina_zindagi_se(request):
	text = Sargams.objects.filter(id__iexact =425)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Tere_bina_jiya_jaye_na(request):
	text = Sargams.objects.filter(id__iexact =426)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Tere_bin_tere_bin(request):
	text = Sargams.objects.filter(id__iexact =427)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Tere_bin_nayi_lagda_dil_mera_dholna(request):
	text = Sargams.objects.filter(id__iexact =428)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Tanhayee(request):
	text = Sargams.objects.filter(id__iexact =429)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Tadap_Tadap_ke_is_dil_se(request):
	text = Sargams.objects.filter(id__iexact =430)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Shyam_teri_bansi(request):
	text = Sargams.objects.filter(id__iexact =431)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Suno_na_sange_marmar_ki(request):
	text = Sargams.objects.filter(id__iexact =432)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Sunn_raha_hai_na_tu(request):
	text = Sargams.objects.filter(id__iexact =433)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Solah_baras_ki_bali_umar_ko_salam(request):
	text = Sargams.objects.filter(id__iexact =434)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Seene_me_jalan(request):
	text = Sargams.objects.filter(id__iexact =435)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Suno_gaur_sey_duniya_walon(request):
	text = Sargams.objects.filter(id__iexact =436)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Sawan_ka_mahina(request):
	text = Sargams.objects.filter(id__iexact =437)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Saranga_teri_yaad_me(request):
	text = Sargams.objects.filter(id__iexact =438)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Sathiya_tune_kya_kiya(request):
	text = Sargams.objects.filter(id__iexact =439)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Sapne_me_sajan_se_do_batein(request):
	text = Sargams.objects.filter(id__iexact =440)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Satyam_Shivam_Sundaram(request):
	text = Sargams.objects.filter(id__iexact =441)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Sanwaar_loon(request):
	text = Sargams.objects.filter(id__iexact =442)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Saiyyan__Heere_Moti_main_na_chahu_(request):
	text = Sargams.objects.filter(id__iexact =443)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Roop_tera_mastana(request):
	text = Sargams.objects.filter(id__iexact =444)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Rasik_Balma(request):
	text = Sargams.objects.filter(id__iexact =445)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Rimjhim_Rimjhim_Rumjhum_Rumjhum(request):
	text = Sargams.objects.filter(id__iexact =446)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Sanam_Re_sanam_re(request):
	text = Sargams.objects.filter(id__iexact =447)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Rang_Barse_Bhige_Chunar_Wali(request):
	text = Sargams.objects.filter(id__iexact =448)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Ranjish_Hi_Sahi(request):
	text = Sargams.objects.filter(id__iexact =449)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Raat_Kali_ek_khwaab_mein_aayee(request):
	text = Sargams.objects.filter(id__iexact =450)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Pukarta_chalaa_hun_mein(request):
	text = Sargams.objects.filter(id__iexact =451)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Puchho_na_kaise_maine_rain_bitai(request):
	text = Sargams.objects.filter(id__iexact =452)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Piya_to_se_naina_lage_re(request):
	text = Sargams.objects.filter(id__iexact =453)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Piya_Re_Piya_Re(request):
	text = Sargams.objects.filter(id__iexact =454)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Phoolon_Ka_Taron_Ka(request):
	text = Sargams.objects.filter(id__iexact =455)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Pehla_nasha_pehla_khumar(request):
	text = Sargams.objects.filter(id__iexact =456)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Pardesiya_ye_sach_hai_piya(request):
	text = Sargams.objects.filter(id__iexact =457)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Pani_da_rang_wekh_ke(request):
	text = Sargams.objects.filter(id__iexact =458)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Pankh_Hote_Toh_Udd_Aati_Re(request):
	text = Sargams.objects.filter(id__iexact =459)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Pal_Pal_Pal(request):
	text = Sargams.objects.filter(id__iexact =460)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Pal_pal_dil_ke_paas(request):
	text = Sargams.objects.filter(id__iexact =461)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_O_saathi_re(request):
	text = Sargams.objects.filter(id__iexact =462)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_O_Sajnaa__barakha_bahaar_aayee(request):
	text = Sargams.objects.filter(id__iexact =463)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_O_ri_chiraiya(request):
	text = Sargams.objects.filter(id__iexact =464)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_O_Re_Piya(request):
	text = Sargams.objects.filter(id__iexact =465)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_O_re_manva_tu_kyu_bavra_hai__Iktara_(request):
	text = Sargams.objects.filter(id__iexact =466)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_O_mere_dil_ke_chain(request):
	text = Sargams.objects.filter(id__iexact =467)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_O_majhi_re(request):
	text = Sargams.objects.filter(id__iexact =468)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_O_hansini(request):
	text = Sargams.objects.filter(id__iexact =469)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Neela_asman_so_gaya(request):
	text = Sargams.objects.filter(id__iexact =470)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Nanha_Munna_Rahi_Hu(request):
	text = Sargams.objects.filter(id__iexact =471)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Naina_Barse_Rim_jhim_Rim_jhim(request):
	text = Sargams.objects.filter(id__iexact =472)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Naino_me_badra_chhaye(request):
	text = Sargams.objects.filter(id__iexact =473)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Neele_Gagan_Ke_Tale(request):
	text = Sargams.objects.filter(id__iexact =474)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Nahi_Nahi_Abhi_Nahi(request):
	text = Sargams.objects.filter(id__iexact =475)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Nadiya_se_Dariya(request):
	text = Sargams.objects.filter(id__iexact =476)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Surmayee_ankhiyon_me(request):
	text = Sargams.objects.filter(id__iexact =477)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Musafir_Hu_Yaro(request):
	text = Sargams.objects.filter(id__iexact =478)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Mohabbaten_Lutaungaa(request):
	text = Sargams.objects.filter(id__iexact =479)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Mujhko_is_raat_ki_tanhayi_me(request):
	text = Sargams.objects.filter(id__iexact =480)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Meri_bhigi_bhigi_si(request):
	text = Sargams.objects.filter(id__iexact =481)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Mitwa__Mere_man_ye_bata_de_tu_(request):
	text = Sargams.objects.filter(id__iexact =482)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Mere_rashk_e_kamar(request):
	text = Sargams.objects.filter(id__iexact =483)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Mere_Rang_Mein_rangne_wali(request):
	text = Sargams.objects.filter(id__iexact =484)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Mere_Nishaan__OMG_(request):
	text = Sargams.objects.filter(id__iexact =485)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Mere_naina_sawan_bhadon(request):
	text = Sargams.objects.filter(id__iexact =486)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Mere_khwabo_me_jo_aye(request):
	text = Sargams.objects.filter(id__iexact =487)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Mere_mehboob_qayamat_hogi(request):
	text = Sargams.objects.filter(id__iexact =488)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Mere_hath_mein(request):
	text = Sargams.objects.filter(id__iexact =489)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Mera_mulk_mera_desh(request):
	text = Sargams.objects.filter(id__iexact =490)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Mere_dil_me_aj_kya_hai(request):
	text = Sargams.objects.filter(id__iexact =491)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Manwa_Lage(request):
	text = Sargams.objects.filter(id__iexact =492)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Megha_chhaye_aadhi_raat(request):
	text = Sargams.objects.filter(id__iexact =493)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Man_re_tu_kahe_na_dhir_dhare(request):
	text = Sargams.objects.filter(id__iexact =494)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Main_tenu_samjhawa_ki(request):
	text = Sargams.objects.filter(id__iexact =495)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Man_Mast_Magan(request):
	text = Sargams.objects.filter(id__iexact =496)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Main_rahu_ya_na_rahu(request):
	text = Sargams.objects.filter(id__iexact =497)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Main_Kabhi_Batlata_Nahin__Maa_(request):
	text = Sargams.objects.filter(id__iexact =498)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Mai_ye_soch_kar_uske_dar_se(request):
	text = Sargams.objects.filter(id__iexact =499)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Lukka_chuppi(request):
	text = Sargams.objects.filter(id__iexact =500)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Mai_shayar_badnam(request):
	text = Sargams.objects.filter(id__iexact =501)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Madhosh_dil_ki_dhadkan(request):
	text = Sargams.objects.filter(id__iexact =502)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Laila_main_laila(request):
	text = Sargams.objects.filter(id__iexact =503)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Lag_Ja_Gale(request):
	text = Sargams.objects.filter(id__iexact =504)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Kyuki_Tum_Hi_Ho(request):
	text = Sargams.objects.filter(id__iexact =505)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Lambi_Judaai(request):
	text = Sargams.objects.filter(id__iexact =506)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Kuhu_Kuhu_bole_koyaliya(request):
	text = Sargams.objects.filter(id__iexact =507)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Kyu_na_bole_mose_mohan_kyu(request):
	text = Sargams.objects.filter(id__iexact =508)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Kya_yehi_pyar_hai(request):
	text = Sargams.objects.filter(id__iexact =509)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Kurbaan_Hua(request):
	text = Sargams.objects.filter(id__iexact =510)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Kora_Kagaz_Tha_Yeh_Mann_Mera(request):
	text = Sargams.objects.filter(id__iexact =511)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Koi_Humdum_Na_Raha(request):
	text = Sargams.objects.filter(id__iexact =512)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Koi_ye_kaise_bataaye(request):
	text = Sargams.objects.filter(id__iexact =513)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Kiska_rasta_dekhe(request):
	text = Sargams.objects.filter(id__iexact =514)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Kasme_vade_pyar_wafa_sab(request):
	text = Sargams.objects.filter(id__iexact =515)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Khoya_Khoya_Chand_Khula_Aasman(request):
	text = Sargams.objects.filter(id__iexact =516)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Kaun_hai_jo_sapno_me_aya(request):
	text = Sargams.objects.filter(id__iexact =517)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Muthukodi_Kawadi_Hada(request):
	text = Sargams.objects.filter(id__iexact =518)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Kash_tere_ishq_me_nilam_ho_jau(request):
	text = Sargams.objects.filter(id__iexact =519)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Kariye_Na_Kariye_Na(request):
	text = Sargams.objects.filter(id__iexact =520)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Kal_ho_na_ho__Har_ghadi_badal_rahi_hai____(request):
	text = Sargams.objects.filter(id__iexact =521)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Kahin_door_jab_din_dhal_jaye(request):
	text = Sargams.objects.filter(id__iexact =522)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Kabhi_Sham_Dhale(request):
	text = Sargams.objects.filter(id__iexact =523)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Kahin_Karti_Hogi(request):
	text = Sargams.objects.filter(id__iexact =524)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Kaha_tak_ye_man_ko(request):
	text = Sargams.objects.filter(id__iexact =525)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Kabhi_kabhi_mere_dil_me(request):
	text = Sargams.objects.filter(id__iexact =526)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Ka_Karu_Sajni_Aye_na_baalam(request):
	text = Sargams.objects.filter(id__iexact =527)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Jogi_Jab_Se_Yu_Aya_Mere_Dware(request):
	text = Sargams.objects.filter(id__iexact =528)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Jeene_Laga_Hoon(request):
	text = Sargams.objects.filter(id__iexact =529)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Jeena_Yahan_Merna_Yahan(request):
	text = Sargams.objects.filter(id__iexact =530)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Jeena_Jeena(request):
	text = Sargams.objects.filter(id__iexact =531)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Jaun_kahan_bata_aye_dil(request):
	text = Sargams.objects.filter(id__iexact =532)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Jashn_e_bahara(request):
	text = Sargams.objects.filter(id__iexact =533)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Janeman_Janeman_Tere_Do_Nayan(request):
	text = Sargams.objects.filter(id__iexact =534)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Jane_Woh_Kaise_Log_The(request):
	text = Sargams.objects.filter(id__iexact =535)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Jane_kyu_log_mohabbat_kiya_karte_ha(request):
	text = Sargams.objects.filter(id__iexact =536)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Jane_kya_dhoondti_rehti_hai(request):
	text = Sargams.objects.filter(id__iexact =537)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Jane_Kahan_Gaye_Wo_Din(request):
	text = Sargams.objects.filter(id__iexact =538)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Jane_do_na__Paas_aao_na(request):
	text = Sargams.objects.filter(id__iexact =539)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Janam_janam_janam(request):
	text = Sargams.objects.filter(id__iexact =540)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Jai_jai_shiv_shankar(request):
	text = Sargams.objects.filter(id__iexact =541)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Jaane_Kya_Baat_Hai(request):
	text = Sargams.objects.filter(id__iexact =542)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Jaane_ja_dhundhta_fir_raha(request):
	text = Sargams.objects.filter(id__iexact =543)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Jab_koi_baat_bigad_jaaye(request):
	text = Sargams.objects.filter(id__iexact =544)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Itni_shakti_hame_dena_daata(request):
	text = Sargams.objects.filter(id__iexact =545)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Itna_na_mujhase_tu_pyar_badha(request):
	text = Sargams.objects.filter(id__iexact =546)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Isharo_isharo_me_dil_lene_wale(request):
	text = Sargams.objects.filter(id__iexact =547)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Ik_hasee_shaam_ko(request):
	text = Sargams.objects.filter(id__iexact =548)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Ik_aisi_ladki_thi(request):
	text = Sargams.objects.filter(id__iexact =549)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Hum_tere_sheher_me_aye_hai(request):
	text = Sargams.objects.filter(id__iexact =550)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Hum_rahe_ya_na_rahe_kal(request):
	text = Sargams.objects.filter(id__iexact =551)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Hum_tere_bin_ab_jee_nahi_sakte__Kyuki_Tum_hi_ho_(request):
	text = Sargams.objects.filter(id__iexact =552)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Humma_humma__ik_ho_gaye_hum_aur_tum_(request):
	text = Sargams.objects.filter(id__iexact =553)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Hum_dono_do_premi(request):
	text = Sargams.objects.filter(id__iexact =554)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Hum_dil_de_chuke_sanam(request):
	text = Sargams.objects.filter(id__iexact =555)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Hum_Bewafa_Hargeez_Na_The(request):
	text = Sargams.objects.filter(id__iexact =556)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Hum_Aapke_Hain_Kaun(request):
	text = Sargams.objects.filter(id__iexact =557)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Hothon_se_chhoo_lo_tum(request):
	text = Sargams.objects.filter(id__iexact =558)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Hoshwalo_ko_khabar_kya(request):
	text = Sargams.objects.filter(id__iexact =559)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Har_kisi_ko_nahi_milta__Do_Lafz_ki_hai_(request):
	text = Sargams.objects.filter(id__iexact =560)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Hame_tumse_pyaar_kitna(request):
	text = Sargams.objects.filter(id__iexact =561)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Hamari_Adhuri_Kahani__Title_Song_(request):
	text = Sargams.objects.filter(id__iexact =562)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Hai_apna_dil_to_awara(request):
	text = Sargams.objects.filter(id__iexact =563)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Gumnam_hai_koi(request):
	text = Sargams.objects.filter(id__iexact =564)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Gulabi_ankhen_jo_teri_dekhi(request):
	text = Sargams.objects.filter(id__iexact =565)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Ghar_jayegi_tar_jayegi(request):
	text = Sargams.objects.filter(id__iexact =566)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Ghar_Aaya_Mera_Pardesi(request):
	text = Sargams.objects.filter(id__iexact =567)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Gerua__Dhoop_se_nikal_ke_(request):
	text = Sargams.objects.filter(id__iexact =568)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Ek_daal_par_tota_bole(request):
	text = Sargams.objects.filter(id__iexact =569)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Ek_Ajnabi_Haseena_Se(request):
	text = Sargams.objects.filter(id__iexact =570)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Ek_Ladki_ko_dekha_to(request):
	text = Sargams.objects.filter(id__iexact =571)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Doston_se_jhooti_mooti(request):
	text = Sargams.objects.filter(id__iexact =572)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Doraemon_theme_song__Hindi_(request):
	text = Sargams.objects.filter(id__iexact =573)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Doli_me_bithai_ke_kahar(request):
	text = Sargams.objects.filter(id__iexact =574)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Do_Lafzon_Ki_Hai(request):
	text = Sargams.objects.filter(id__iexact =575)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Dil_Smbhal_ja_zara(request):
	text = Sargams.objects.filter(id__iexact =576)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Din_dhal_jaye(request):
	text = Sargams.objects.filter(id__iexact =577)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Dil_Pukare_Aare_Aare_Aare(request):
	text = Sargams.objects.filter(id__iexact =578)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Dil_ne_kaha_chupke_se(request):
	text = Sargams.objects.filter(id__iexact =579)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Dil_hai_chota_sa(request):
	text = Sargams.objects.filter(id__iexact =580)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Dil_Hoom_Hoom_Kare(request):
	text = Sargams.objects.filter(id__iexact =581)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Dil_diydiyan_gallan(request):
	text = Sargams.objects.filter(id__iexact =582)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Dil_diya_hai_jaan_bhi_denge(request):
	text = Sargams.objects.filter(id__iexact =583)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Dhadkan_zara_ruk_gayi_hai(request):
	text = Sargams.objects.filter(id__iexact =584)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Dekha_Na_Haay_Re(request):
	text = Sargams.objects.filter(id__iexact =585)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Deewana_hua_baadal(request):
	text = Sargams.objects.filter(id__iexact =586)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Dard_dilo_ke_kam_ho_jate(request):
	text = Sargams.objects.filter(id__iexact =587)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Chura_liya_hai_tumne_jo(request):
	text = Sargams.objects.filter(id__iexact =588)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Chori_chori_teri_meri_love_story(request):
	text = Sargams.objects.filter(id__iexact =589)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Chupke_Chupke_Raat_Din(request):
	text = Sargams.objects.filter(id__iexact =590)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Chingari_koyi_bhadake(request):
	text = Sargams.objects.filter(id__iexact =591)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Choodi_nahi_ye_mera(request):
	text = Sargams.objects.filter(id__iexact =592)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Chup_chup_khade_ho(request):
	text = Sargams.objects.filter(id__iexact =593)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Chhoo_kar_mere_man_ko(request):
	text = Sargams.objects.filter(id__iexact =594)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Chehra_hai_ya_chand_khila(request):
	text = Sargams.objects.filter(id__iexact =595)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Chak_Dhoom_Dhoom_____Koi_Ladki_Hai_Jab_Wo_Hasti_Hai_(request):
	text = Sargams.objects.filter(id__iexact =596)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Chandan_sa_badan(request):
	text = Sargams.objects.filter(id__iexact =597)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Chaha_tujhe_hai__Band_of_Boys_(request):
	text = Sargams.objects.filter(id__iexact =598)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Chaha_Hai_Tujhko(request):
	text = Sargams.objects.filter(id__iexact =599)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Breathless(request):
	text = Sargams.objects.filter(id__iexact =600)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Bolna_Mahi_Bolna(request):
	text = Sargams.objects.filter(id__iexact =601)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Bhor_bhaye_panghat_pe(request):
	text = Sargams.objects.filter(id__iexact =602)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Bhigi_bhigi_rato_me(request):
	text = Sargams.objects.filter(id__iexact =603)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Bheegi_Bheegi_Si_Hai_Raatein(request):
	text = Sargams.objects.filter(id__iexact =604)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Bheege_hont_tere(request):
	text = Sargams.objects.filter(id__iexact =605)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Bavra_Mann_Dekhne_Chala_Ek_Sapna(request):
	text = Sargams.objects.filter(id__iexact =606)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Bechara_dil_kya_kare(request):
	text = Sargams.objects.filter(id__iexact =607)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Aise_na_mujhe_tum_dekho(request):
	text = Sargams.objects.filter(id__iexact =608)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Ahatein_ho_rahi_teri__MTV_Splitsvilla_(request):
	text = Sargams.objects.filter(id__iexact =609)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Abhi_naa_jao_chhod_kar(request):
	text = Sargams.objects.filter(id__iexact =610)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Ae_Zindagi_Gale_Laga_Le(request):
	text = Sargams.objects.filter(id__iexact =611)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Abhi_mujh_mein_kahin(request):
	text = Sargams.objects.filter(id__iexact =612)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Ab_To_Hai_Tumse(request):
	text = Sargams.objects.filter(id__iexact =613)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Aate_jate_hanste_gaate(request):
	text = Sargams.objects.filter(id__iexact =614)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Aaoge_jab_tum_o_saajna(request):
	text = Sargams.objects.filter(id__iexact =615)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Aao_na_gale_lagalo_na(request):
	text = Sargams.objects.filter(id__iexact =616)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Aap_ke_haseen_rukh_pe(request):
	text = Sargams.objects.filter(id__iexact =617)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Chhupa_Lo_yun_Dil_me(request):
	text = Sargams.objects.filter(id__iexact =618)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Aane_wala_pal_jane_wala_hai(request):
	text = Sargams.objects.filter(id__iexact =619)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notes___Sargam_Gerua__Dilwale_(request):
	text = Sargams.objects.filter(id__iexact =620)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Tum_Hi_Aana__Marjaavaan_(request):
	text = Sargams.objects.filter(id__iexact =621)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Nanha_Munna_Rahi_Hoon__Son_Of_India_(request):
	text = Sargams.objects.filter(id__iexact =622)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Dil_De_Diya_Hain__Anand_Raj_Anand_(request):
	text = Sargams.objects.filter(id__iexact =623)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Teri_Meri_Kahani__Happy_Hardy_And_Heer_(request):
	text = Sargams.objects.filter(id__iexact =624)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Shikwa_Nahi__Jubin_Nautiyal_(request):
	text = Sargams.objects.filter(id__iexact =625)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Mere_Saamne_Wali_Khidhi_Mein__Padosan_(request):
	text = Sargams.objects.filter(id__iexact =626)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Thodi_Jagah__Marjaavaan_(request):
	text = Sargams.objects.filter(id__iexact =627)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Mere_Mehboob_Qayamat_Hogi__Kishore_Kumar_(request):
	text = Sargams.objects.filter(id__iexact =628)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Surili_Akhiyon_Wale__Veer_(request):
	text = Sargams.objects.filter(id__iexact =629)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Chura_Liya_Hai_Tumne_Jo_Dil_Ko__Yaadon_Ki_Baaraat_(request):
	text = Sargams.objects.filter(id__iexact =630)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Duniyaa__Luka_Chuppi_(request):
	text = Sargams.objects.filter(id__iexact =631)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Pyar_Diwana_Hota_Hai__Kati_Patang_(request):
	text = Sargams.objects.filter(id__iexact =632)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Phoolon_Ka_Taaron_Ka__Hare_Rama_Hare_Krishna_(request):
	text = Sargams.objects.filter(id__iexact =633)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Raabta__Agent_Vinod___Full_Song_(request):
	text = Sargams.objects.filter(id__iexact =634)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Dil_Mein_Ho_Tum__Why_Cheat_India_(request):
	text = Sargams.objects.filter(id__iexact =635)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Sanu_Ek_Pal_Chain__Raid_(request):
	text = Sargams.objects.filter(id__iexact =636)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Gulabi_Ankhen__The_Train_(request):
	text = Sargams.objects.filter(id__iexact =637)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Ek_Ajnabee_Haseena_Se__Ajnabee_(request):
	text = Sargams.objects.filter(id__iexact =638)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Aadat__Jal_(request):
	text = Sargams.objects.filter(id__iexact =639)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Kuch_Kuch_Hota_Hai__Title_Song_(request):
	text = Sargams.objects.filter(id__iexact =640)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Achyutam_Keshavam(request):
	text = Sargams.objects.filter(id__iexact =641)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Dekha_Hazaro_Dafaa__Rustom_(request):
	text = Sargams.objects.filter(id__iexact =642)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Kalank__Title_Track_(request):
	text = Sargams.objects.filter(id__iexact =643)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Nani_Teri_Morni_Ko_Mor_Le_Gaye(request):
	text = Sargams.objects.filter(id__iexact =644)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Main_Hoon_Hero_Tera__Salman_Khan_(request):
	text = Sargams.objects.filter(id__iexact =645)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Pachtaoge__Arijit_Singh_(request):
	text = Sargams.objects.filter(id__iexact =646)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Luka_Chuppi__Lata_Mangeshkar_(request):
	text = Sargams.objects.filter(id__iexact =647)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Hawayein__Jab_Harry_Met_Sejal_(request):
	text = Sargams.objects.filter(id__iexact =648)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Banjaara__Ek_Villain_(request):
	text = Sargams.objects.filter(id__iexact =649)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Jiya_Dhadak_Dhadak_Jaye__Kalyug_(request):
	text = Sargams.objects.filter(id__iexact =650)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Mile_Ho_Tum__Fever_(request):
	text = Sargams.objects.filter(id__iexact =651)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Maa__Taare_Zameen_Par_(request):
	text = Sargams.objects.filter(id__iexact =652)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_The_Jungle_Book__Title_Song_(request):
	text = Sargams.objects.filter(id__iexact =653)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Afreen_Afreen__Coke_Studio_(request):
	text = Sargams.objects.filter(id__iexact =654)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Jab_Se_Tere_Naina__Saawariya_(request):
	text = Sargams.objects.filter(id__iexact =655)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Jeena_Jeena__Full_Song___Badlapur_(request):
	text = Sargams.objects.filter(id__iexact =656)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Bum_Bum_Bole__Taare_Zameen_Par_(request):
	text = Sargams.objects.filter(id__iexact =657)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Sare_Jahan_Se_Achaa(request):
	text = Sargams.objects.filter(id__iexact =658)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Tum_Hi_Ho__Aashiqui_2_(request):
	text = Sargams.objects.filter(id__iexact =659)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Bolna__Kapoor_And_Sons_(request):
	text = Sargams.objects.filter(id__iexact =660)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Yaaron_Dosti_Badi_Hi__K_K__(request):
	text = Sargams.objects.filter(id__iexact =661)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Sau_Dard_Hai__Jaan_E_Mann_(request):
	text = Sargams.objects.filter(id__iexact =662)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Tu_Hi_Haqeeqat__Tum_Mile_(request):
	text = Sargams.objects.filter(id__iexact =663)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Zindagi_Do_Pal_Ki__Kites_(request):
	text = Sargams.objects.filter(id__iexact =664)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Dil_Kyun_Yeh_Mera__Kites_(request):
	text = Sargams.objects.filter(id__iexact =665)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Tu_Jaane_Na__Ajab_Prem_Ki_Ghazab_Kahani_(request):
	text = Sargams.objects.filter(id__iexact =666)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Lakdi_Ki_Kaathi__Masoom_(request):
	text = Sargams.objects.filter(id__iexact =667)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Kaise_Hua__Kabir_Singh_(request):
	text = Sargams.objects.filter(id__iexact =668)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Channa_Mereya__Ae_Dil_Hai_Mushkil_(request):
	text = Sargams.objects.filter(id__iexact =669)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Tujhe_Dekha_To_Yeh_Jana_Sanam__DDLJ_(request):
	text = Sargams.objects.filter(id__iexact =670)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Tera_Ban_Jaunga__Kabir_Singh_(request):
	text = Sargams.objects.filter(id__iexact =671)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Namo_Namo__Kedarnath_(request):
	text = Sargams.objects.filter(id__iexact =672)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Tera_Ghata__Gajendra_Verma_(request):
	text = Sargams.objects.filter(id__iexact =673)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Main_Jahaan_Rahoon__Namastey_London_(request):
	text = Sargams.objects.filter(id__iexact =674)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Mere_Rashke_Qamar__Baadshaho_(request):
	text = Sargams.objects.filter(id__iexact =675)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Barso_Re_Megha_Megha__Guru_(request):
	text = Sargams.objects.filter(id__iexact =676)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Janam_Janam__Dilwale_(request):
	text = Sargams.objects.filter(id__iexact =677)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Hothon_Se_Chhulo_Tum__Jagjit_Singh_(request):
	text = Sargams.objects.filter(id__iexact =678)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Tera_Yaar_Hoon_Main__Sonu_Ke_Tittu_Ki_Sweety_(request):
	text = Sargams.objects.filter(id__iexact =679)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Yaara_Teri_Yaari(request):
	text = Sargams.objects.filter(id__iexact =680)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Aaoge_Jab_Tum__Jab_We_Met_(request):
	text = Sargams.objects.filter(id__iexact =681)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Basabriyaan__M_S__Dhoni(request):
	text = Sargams.objects.filter(id__iexact =682)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def The_Untold_Story_(request):
	text = Sargams.objects.filter(id__iexact =683)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Bekhayali__Kabir_Singh_(request):
	text = Sargams.objects.filter(id__iexact =684)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Ajj_Din_Chadheya__Love_Aaj_Kal_(request):
	text = Sargams.objects.filter(id__iexact =685)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Tujhko_Jo_Paaya__Crook_(request):
	text = Sargams.objects.filter(id__iexact =686)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Abhi_Mujh_Mein_Kahin__Agneepath_(request):
	text = Sargams.objects.filter(id__iexact =687)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Dhadak__Title_Song_(request):
	text = Sargams.objects.filter(id__iexact =688)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Ishq_Sufiana__The_Dirty_Picture_(request):
	text = Sargams.objects.filter(id__iexact =689)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Vaaste__Dhvani_Bhanushali___Full_Song_(request):
	text = Sargams.objects.filter(id__iexact =690)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Phir_Kabhi__M_S__Dhoni_(request):
	text = Sargams.objects.filter(id__iexact =691)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Zaalima__Raees_(request):
	text = Sargams.objects.filter(id__iexact =692)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Har_Kisi_Ko_Nahi_Milta_Yahan_Pyaar_Zindgi_Mein__Boss_(request):
	text = Sargams.objects.filter(id__iexact =693)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Dil_Diyan_Gallan__Tiger_Zinda_Hai_(request):
	text = Sargams.objects.filter(id__iexact =694)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Tujh_Mein_Rab_Dikhta_Hai__Rab_Ne_Banadi_Jodi__(request):
	text = Sargams.objects.filter(id__iexact =695)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Tu_Hai_Ki_Nahi__Roy_(request):
	text = Sargams.objects.filter(id__iexact =696)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Mast_Magan__2_States_(request):
	text = Sargams.objects.filter(id__iexact =697)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Maana_Ke_Hum_Yaar_Nahi__Meri_Pyaari_Bindu_(request):
	text = Sargams.objects.filter(id__iexact =698)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Sanam_Re__Tile_Song_(request):
	text = Sargams.objects.filter(id__iexact =699)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Tujhe_Kitna_Chahne_Lage__Kabir_Singh_(request):
	text = Sargams.objects.filter(id__iexact =700)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Girl_I_Need_You__Baaghi_(request):
	text = Sargams.objects.filter(id__iexact =701)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Mujhe_Kaise_Pata_Na_Chala__Papon_(request):
	text = Sargams.objects.filter(id__iexact =702)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Maula_Mera_Le_Le_Meri_Jann__Chak_De_India_(request):
	text = Sargams.objects.filter(id__iexact =703)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Har_Ghadi__Kal_Ho_Na_Ho_(request):
	text = Sargams.objects.filter(id__iexact =704)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Jee_Le_Zara__Talaash_(request):
	text = Sargams.objects.filter(id__iexact =705)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Zara_Zara__RHTDM_(request):
	text = Sargams.objects.filter(id__iexact =706)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Iktara__Wake_Up_Sid_(request):
	text = Sargams.objects.filter(id__iexact =707)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Kabhi_Jo_Badal_Barse__Jackpot_(request):
	text = Sargams.objects.filter(id__iexact =708)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Tune_Mere_Jaana__Emptiness_(request):
	text = Sargams.objects.filter(id__iexact =709)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Ve_maahi__Kesari_(request):
	text = Sargams.objects.filter(id__iexact =710)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Mitwa__Kabhi_Alvida_Na_Kehna_(request):
	text = Sargams.objects.filter(id__iexact =711)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Bhagwan_Hain_Kahan_Re_Tu_(request):
	text = Sargams.objects.filter(id__iexact =712)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam__And_Flute_Aao_Na(request):
	text = Sargams.objects.filter(id__iexact =713)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Vaaste__Dhvani_Bhanushali_(request):
	text = Sargams.objects.filter(id__iexact =714)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_and_Flute_Pyaar_Ke_Pal__K_K____Sargam_And_Flute_Tum_Se_Hi__Jab_We_Met_(request):
	text = Sargams.objects.filter(id__iexact =715)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Meherbaani(request):
	text = Sargams.objects.filter(id__iexact =716)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Choo_Lo__The_Local_Train_(request):
	text = Sargams.objects.filter(id__iexact =717)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Kuch_Is_Taraha__Doorie_(request):
	text = Sargams.objects.filter(id__iexact =718)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Emptiness(request):
	text = Sargams.objects.filter(id__iexact =719)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Teri_Mitti_(request):
	text = Sargams.objects.filter(id__iexact =720)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Indian_Flute_And_Sargam_Te_Amo(request):
	text = Sargams.objects.filter(id__iexact =721)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Laadki(request):
	text = Sargams.objects.filter(id__iexact =722)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Muskurane(request):
	text = Sargams.objects.filter(id__iexact =723)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Pee_Loon(request):
	text = Sargams.objects.filter(id__iexact =724)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Game_Of_Thrones(request):
	text = Sargams.objects.filter(id__iexact =725)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Perfect__Ed_Sheeran_(request):
	text = Sargams.objects.filter(id__iexact =726)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_See_You_Again_ft__Charlie_Puth__Wiz_Khalifa_(request):
	text = Sargams.objects.filter(id__iexact =727)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Rive_Flow_In_You__Yiruma_(request):
	text = Sargams.objects.filter(id__iexact =728)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Pirates_Of_The_Caribbean(request):
	text = Sargams.objects.filter(id__iexact =729)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Harry_Potter__Theme_Song_(request):
	text = Sargams.objects.filter(id__iexact =730)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_On_My_Way__Alan_Walker_(request):
	text = Sargams.objects.filter(id__iexact =731)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_The_Last_Of_Mohicans_(request):
	text = Sargams.objects.filter(id__iexact =732)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Jingle_Bells(request):
	text = Sargams.objects.filter(id__iexact =733)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Doraemon___Zindagi_Sawarn_Doon_(request):
	text = Sargams.objects.filter(id__iexact =734)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Happy_Birthday(request):
	text = Sargams.objects.filter(id__iexact =735)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Fadad__Alan_Walker_(request):
	text = Sargams.objects.filter(id__iexact =736)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Moh_Moh_ke_dhaage__Dum_Laga_Ke_Haisha_(request):
	text = Sargams.objects.filter(id__iexact =737)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Yeh_Aaina__Kabir_Singh_(request):
	text = Sargams.objects.filter(id__iexact =738)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Yaara__Mamta_Sharma_(request):
	text = Sargams.objects.filter(id__iexact =739)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Samjhawan__Humpty_Sharma_Ki_Dulhania_(request):
	text = Sargams.objects.filter(id__iexact =740)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Tu_Mileya__Darshan_Raval_(request):
	text = Sargams.objects.filter(id__iexact =741)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Intezaar__Arijit_Singh_(request):
	text = Sargams.objects.filter(id__iexact =742)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sargam_And_Flute_Dekhte_Dekhte__Batti_Gul_Meter_Chalu_(request):
	text = Sargams.objects.filter(id__iexact =743)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

