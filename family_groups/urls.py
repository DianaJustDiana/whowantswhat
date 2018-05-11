"""Defines URL patterns for family_groups app."""
from django.urls import path
from . import views
##from django.conf import settings
##from django.conf.urls.static import static

app_name = 'family_groups'

urlpatterns = [
    #User can create a family group.
    path('create_a_family/', views.create_a_family, name='create_a_family'),
    #User can add members to the family group.
    path('add_members/', views.add_members, name='add_members'),
]