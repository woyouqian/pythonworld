from django.db import models

# Create your models here.


class Money(models.Model):
    name = models.CharField(max_length=60)
    number = models.CharField(max_length=25)
    charge = models.IntegerField()
    buy = models.IntegerField()
    mark = models.CharField(max_length=110)


