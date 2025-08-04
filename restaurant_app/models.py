from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
    user = models.CharField(max_length=40)
    date = models.CharField(max_length=40)
    time = models.CharField(max_length=40)
    guests = models.IntegerField()
    special_request = models.TextField(blank=True)

 
class Contact(models.Model):
    name= models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    number=models.CharField(max_length=10)
    content=models.TextField(max_length=400)

class Order(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    ordered_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.name

