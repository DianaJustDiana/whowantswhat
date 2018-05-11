"""Defines URL patterns for family_groups app."""
from django.urls import path
from . import views
##from django.conf import settings
##from django.conf.urls.static import static

app_name = 'family_groups'

urlpatterns = [
   
    #Join_a_family_group page for adding new members to family group.
    path('create_a_family/', views.create_a_family, name='create_a_family'),
]