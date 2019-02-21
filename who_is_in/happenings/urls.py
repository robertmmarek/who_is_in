import os 

from django.urls import include, path
from . import views

urlpatterns = [
    path('board/', views.index, name='board'),
    path('profile/', views.index, name='profile')
]