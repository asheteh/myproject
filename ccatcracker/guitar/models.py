from django.db import models


class chords(models.Model):
    song_names = models.TextField(blank=True)
    sargam = models.TextField(blank=True)
    status = models.CharField(max_length=110)
    url = models.CharField(max_length=300,default="old")
   


class chord(models.Model):
    song_names = models.TextField(blank=True)
    sargam = models.TextField(blank=True)
    status = models.CharField(max_length=110)
    url = models.CharField(max_length=200,default="old")
    scale = models.CharField(max_length=200,default="C Major")
    chords = models.CharField(max_length=200,default="C Major,D Minor")
    strum = models.CharField(max_length=200,default="D uud udu")
    meta_key = models.TextField(blank=True,default="new")
    meta_disc = models.TextField(blank=True,default="new")
    meta_disc_os = models.TextField(blank=True,default="new")
    seo = models.TextField(blank=True,default="new")


    def __str__(self):
        return self.song_names



class chor(models.Model):
    song_names = models.TextField(blank=True)
    sargam = models.TextField(blank=True)
    status = models.CharField(max_length=110)
    url = models.CharField(max_length=300,default="old")
   
    def __str__(self):
        return self.song_names


    
class email_subscriptions(models.Model):
    emails  = models.CharField(max_length=200)
    def __str__(self):
        return self.emails


