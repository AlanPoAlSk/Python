from django.urls import path 
from . import views

urlpatterns = [
    path ('', views.index),
    path ('create/dojo', views.create_dojo),
    path ('create/ninja', views.create_ninja),
    path('delete_dojo/<int:dojo_id>/', views.delete_dojo, name='delete_dojo'),
    # path ('create_user', views.create),
]