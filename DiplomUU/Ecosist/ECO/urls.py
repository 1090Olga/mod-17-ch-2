from django.contrib import admin
from django.urls import path
from ECO import views

app_name = 'ECO'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
