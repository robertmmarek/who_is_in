import os 

from django.urls import include, path
from . import views

urlpatterns = [
    path('board/', views.board, name='board'),
    path('profile/', views.profile, name='profile')
]