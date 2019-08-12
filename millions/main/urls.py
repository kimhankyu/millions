#main/url.py
from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.indexView, name='index'),
    path('timer/', views.timerView, name='timer'),
    # path('community/', views.communityView, name='community'),
    path('about/', views.aboutView, name='about'),
    path('data', views.dataView, name='data1'),
    path('data/', views.dataView, name='data2'),
    path('mypage/', views.mypageView, name='mypage'),
]
