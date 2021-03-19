from django.db import models

# Create your models here.
class Destination:
    title:str
    image:str
    order:str
    price:int
    oldprice:int
class firstvalue:
    title:str
    img:str
    price:int
    oldprice:int
    offer:str
    descri:str
    href:str
class RegisteredForms(models.Model):
    uname=models.CharField(max_length=200)
    phone=models.CharField(max_length=13)
    Email=models.EmailField(max_length=200)
    psw=models.CharField(max_length=200)
    psw2=models.CharField(max_length=200)
    

class OrderForm(models.Model):
    product=models.CharField(max_length=200)
    uname=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    Email=models.EmailField(max_length=200)
    address=models.CharField(max_length=300)