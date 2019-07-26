from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.indexView, name='index'),
    path('timer/', views.timerView, name='timer'),
    path('community/', views.communityView, name='community'),
    path('about/', views.aboutView, name='about'),
    
]
