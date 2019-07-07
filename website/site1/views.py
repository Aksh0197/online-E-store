from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.db.models import Subquery
# Create your views here.
def abc(req):
    u=User1.objects.all()
    #req.session["name"]="roshabh"
    return render(req,'site1/myimg.html',{"mydata"})

def login(request):
    mes=""
    if request.method == 'POST':
        if(request.POST.get("psw")==request.POST.get("psw_repeat")):
            u=User1()
            u.email=request.POST.get("email")
            u.pws=request.POST.get("psw")
            u.contact=request.POST.get("contact")
            u.address=request.POST.get("address")
            u.save()
            mes="sucessful"
            request.session["name"]=request.POST.get("email")
            
            
        else:
            
            mes="error"
            
    
    print(mes)
    return render(request,'site1/login.html',{"m":mes})

def signin(request):
    res=""
    if request.method=='POST':
        name=request.POST.get("email1")
        passw=request.POST.get("psw1")
        print(name)
        print(passw)
        
        try:
            u=User1.objects.get(email=name,pws=passw)
            print("match")
            res="successful"
            request.session["name"]=request.POST.get("email1")
            return redirect ("http://127.0.0.1:8000/site1/home")
        except User1.DoesNotExist:
            print("not match")
            res="failed"
            
        
    return render(request,'site1/signin.html',{"a":res})        


def createpost(request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('content'):
                post=Post()
                post.title= request.POST.get('title')
                post.content= request.POST.get('content')
                post.save()
                
                return render(request, 'site1/login1.html')  

        else:
                return render(request,'site1/login1.html')

from .forms import *

def hotel_image_view(request): 
  
    if request.method == 'POST': 
        form = HotelForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = HotelForm() 
    return render(request, 'site1/hotel_image_form.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfuly uploaded') 



# Python program to view 
# for displaying images 

def display_hotel_images(request): 

	if request.method == 'GET': 

		# getting all the objects of hotel. 
		Hotels = Hotel.objects.all() 
		return render(request, 'site1/display_images.html',{'hotel_images' : Hotels})

def cam(request):
    prod=Products.objects.all()
    return render(request, 'site1/cam.html',{'cam' : prod})
def  home(request):
    
    try:

        
        name=request.session["name"]
        if request.method=="POST":
            s=request.POST.get("search2")
            p=Products.objects.filter(product=s)
            print(p)
            return render(request,'site1/home.html',{'data':p})
    except KeyError:
        return redirect('http://127.0.0.1:8000/site1/signin/')
    return render(request,'site1/home.html',{"name":name})
def logout(request):
    del request.session["name"]
    return redirect('http://127.0.0.1:8000/site1/signin/')

def myview(request,question_id):
    return HttpResponse(str(question_id))

def disp(req,id):
    if req.method=='POST':
        id1=req.POST.get("id")
        if req.session.get('name'):
            user=req.session["name"]
        else:
            return redirect('http://127.0.0.1:8000/site1/signin/')
        c=Cart(user_id=user,productid=id1)
        c.save()
    prod=Products.objects.get(id=id)
    return render(req, 'site1/disp.html',{'cam' : prod})

def cart(req):
    
    prod=Cart.objects.all().filter(user_id=req.session["name"])
    p=Products.objects.filter(id__in=Subquery(prod.values('productid')))
    if req.method=='POST':
        prod=Cart.objects.all().filter(user_id=req.session["name"])
        for i in prod:
            a=AddtoCart(user_id=i.user_id,productid=i.productid)
            a.save()
        Cart.objects.all().filter(user_id=req.session["name"]).delete()
    return render(req,'site1/cart.html',{'cam' : p})    
def deletecart(request,id):
    Cart.objects.all().filter(user_id=request.session["name"],productid=id).delete()
    return redirect("http://127.0.0.1:8000/site1/cart/")

