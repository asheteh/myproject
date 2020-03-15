from django.db import models



class Songs(models.Model):
    song_name = models.CharField(max_length=100,blank=True)
    rating = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    singer = models.CharField(max_length=111)
    notation = models.TextField(blank=True)
    link = models.TextField(blank=True)
    
    

class Sargam(models.Model):
    song_names = models.TextField(blank=True)
    sargam = models.TextField(blank=True)
    url = models.TextField(blank=True,default="sd")
    relased = models.CharField(max_length=100,default="dont-know")
    meta_disc =  models.TextField(blank=True,default="music sargams")
    keywords = models.TextField(blank=True,default="music sargams")
    meta_name = models.TextField(blank=True,default="music sargams")
    
    
    

class Sargams(models.Model):
    song_names = models.TextField(blank=True)
    sargam = models.TextField(blank=True)
    url = models.TextField(blank=True)
    relased = models.CharField(max_length=100,default="dont-know")
    meta_disc =  models.TextField(blank=True,default="music sargams")
    keywords = models.TextField(blank=True,default="music sargams")
    meta_name = models.TextField(blank=True,default="music sargams")
    
    def __str__(self):
        return self.song_names
   
    

