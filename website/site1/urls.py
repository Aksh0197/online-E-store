"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from site1 import views

urlpatterns = [
   path('pqr/',views.abc),
   path('login/',views.login),
   path('login1/',views.createpost),
   path('signin/',views.signin),
   path('home/',views.home),
   path('logout/',views.logout),
   path('cam/',views.cam),
   #http://127.0.0.1:8000/site1/my/6
   #http://127.0.0.1:8000/site1/my/5
   #http://127.0.0.1:8000/site1/my/66
   path('disp/<int:id>',views.disp),
   path('del/<int:id>',views.deletecart),
   
   path('cart/',views.cart),
   
   
   
   
]
