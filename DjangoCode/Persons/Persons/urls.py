"""Persons URL Configuration

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
import womans.views as female
# import mans.views as male
from friends import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path(r'friends/', views.friends),
    path(r'add_friend/', views.add_friend),
    path(r'create_friend/', views.create_friend),
    path(r'get_all_friends/', views.get_all_friends),
    path(r'get_all_friends_sex/', views.get_all_friends_sex),
    path(r'get_one_friend/', views.get_one_friend),
    path(r'update_friend/', views.update_friend),
    path(r'delete_friend/', views.delete_friend),
    path(r'search/', views.search),
    path(r'search_friend/', views.search_friend),


    path('', female.index),
    path(r'womans/', female.womans),
    path(r'add_money/', female.add_money),
    path(r'create_money/', female.create_money),
    path(r'get_all_money/', female.get_all_money),
    path(r'get_all_number/', female.get_all_number),
    path(r'get_one_money/', female.get_one_money),
    path(r'update_money/', female.update_money),
    path(r'delete_money/', female.delete_money),
    path(r'search_money/', female.search_money),
    path(r'get_one_detail/', female.get_one_detail),
    path(r'charge_money/', female.charge_money),
    path(r'charge_one_money/', female.charge_one_money),
    path(r'buy_money/', female.buy_money),
    path(r'buy_one_money/', female.buy_one_money),
]

