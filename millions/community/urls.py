#community/urls.py
from django.urls import path
from . import views



urlpatterns = [
    path('community/', views.community, name='community'),
    path('detail/<int:post_id>', views.detail, name='post_detail'),
    path('update/<int:post_id>', views.update, name='update'),
    path('delete/<int:post_id>', views.delete, name='delete'),
]
