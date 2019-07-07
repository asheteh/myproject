from django.db import models

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    amount = models.IntegerField( default=200)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    status = models.CharField(max_length=111,default= 'New')

def __str__(self):
    return self.name