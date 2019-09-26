from django.db import models

# Create your models here.
# friends: name,sex,age,phone,email,do what,address,mark


class Friend(models.Model):
    name = models.CharField(max_length=60)
    sex = models.BooleanField()
    age = models.SmallIntegerField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    live = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mark = models.TextField(max_length=100)



