from django.db import models

# Create your models here.


class Cardsmsg(models.Model):
    hostname = models.CharField(max_length=50)
    cardnumber = models.CharField(max_length=30)
    usepassword = models.CharField(max_length=11)
    mark = models.CharField(max_length=100)

