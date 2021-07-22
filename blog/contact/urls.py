from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #path('contact/', views.contact, name='contact-form'),
    path('contact/', views.ContactView.as_view(), name='contact-form'),
]