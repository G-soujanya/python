"""Defines URL patterns for pizzeria"""
from django.urls import path 
from . import views 
app_name='pizzeria'
urlpatterns=[
    #home page 
    path('',views.index,name='index')
]