from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registerView, name='register'),
    path('aaa/', views.aaa, name='aaa'),
]
