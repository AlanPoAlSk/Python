from django.urls import path 
from . import views

urlpatterns = [
    path ('', views.index),
    path ('create_info', views.create_info),
    path ('result', views.result),
]