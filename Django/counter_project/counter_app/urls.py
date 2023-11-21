from django.urls import path 
from . import views

urlpatterns = [
    path ('', views.index),
    path ('destroy_session', views.destroy),
    path ('plus_two_session', views.plus_two)
]