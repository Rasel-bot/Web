from django.contrib import admin
from django.urls import path
from window import views

urlpatterns = [
    path('', views.index, name='window'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('erp', views.erp, name='erp')

    
]