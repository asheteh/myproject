from django.db import models


class Center(models.Model):
    center_name = models.CharField(max_length=100,blank=True)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    course = models.CharField(max_length=111)
    description = models.TextField(blank=True)
    rank = models.CharField(max_length=111)
    quality = models.CharField(max_length=111)
    placement = models.CharField(max_length=111)
    recommend = models.CharField(max_length=111)
def __str__(self):
    return self.center_name


class Ranks(models.Model):
    center_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    course = models.CharField(max_length=111)
    rank = models.IntegerField()
    placement = models.CharField(max_length=111)
    recommend = models.CharField(max_length=111)
        
def __str__(self):
    return self.center_name

class question(models.Model):
    qno = models.IntegerField()
    task = models.TextField(blank=True)
    ans = models.TextField(blank=True)
    inp  = models.TextField(blank=True)
    out = models.TextField(blank=True)



    
class CCAT_Question(models.Model):
    qno = models.IntegerField()
    question = models.TextField(blank=True)
    ans = models.TextField(blank=True)
    a  = models.CharField(blank=True,max_length=20)
    b = models.CharField(blank=True,max_length=20)
    c  = models.CharField(blank=True,max_length=20)
    d  = models.CharField(blank=True,max_length=20)
    display = models.TextField(blank=True,default = "Yes")

#Notify not using 
class notify(models.Model):
    email =  models.CharField(max_length=100)
    status = models.CharField(max_length=100,default="New")
    


class Aptitude(models.Model):
    qno = models.IntegerField()
    apti_q = models.TextField(blank=True)
    A = models.TextField(blank=True)
    B = models.TextField(blank=True)
    C  = models.TextField(blank=True)
    D = models.TextField(blank=True)
    ans = models.TextField(blank=True)


class Send(models.Model):
    email = models.CharField(max_length=111)
       
       
    status = models.CharField(max_length=111,default= 'New')


class SendEmail(models.Model):
        email = models.CharField(max_length=111,unique=True)
        status = models.CharField(max_length=111,default= 'New')
