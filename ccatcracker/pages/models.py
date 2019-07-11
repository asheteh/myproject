from django.db import models


class Center(models.Model):
    center_name = models.CharField(max_length=100)
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