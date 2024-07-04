# menu/urls.py
from django.urls import path
from . import views

app_name = 'forms' # Define el namespace

urlpatterns = [
    path('', views.index, name='form'),

]

