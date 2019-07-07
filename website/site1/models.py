from django.db import models

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=300, unique=True)
    content= models.TextField()
class User1(models.Model):
    email= models.CharField(max_length=300, unique=True)
    pws= models.CharField(max_length=300, unique=True)
    contact=models.CharField(max_length=300, unique=True)
    address=models.CharField(max_length=300, unique=True)
# models.py 
class Hotel(models.Model): 
	name = models.CharField(max_length=50) 
	hotel_Main_Img = models.ImageField(upload_to='images/') 

class Products(models.Model):
    product=models.CharField(max_length=300, unique=True)
    model=models.CharField(max_length=300, unique=True)
    price=models.CharField(max_length=300, unique=True)
    quantity=models.CharField(max_length=300, unique=True)
    product_img = models.ImageField(upload_to='images/') 
    
class Cart(models.Model):
    user_id=models.CharField(max_length=300)
    productid=models.IntegerField()

class AddtoCart(models.Model):
    user_id=models.CharField(max_length=300)
    productid=models.IntegerField()
    date=models.DateField(null=False, blank=False, auto_now=True)