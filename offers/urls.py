"""Defines URL patterns for offers app."""
from django.urls import path
from . import views
##from django.conf import settings
##from django.conf.urls.static import static

app_name = 'offers'

urlpatterns = [
    #Home page for offers app.
    path('', views.index, name='index'),
    #New_offer page for adding new offers.
    path('new_offer/', views.new_offer, name='new_offer'),
    path('available_to_me/', views.available_to_me, name='available_to_me'),
    path('available_to_me/add_dib', views.add_dib, name='add_dib'),
]