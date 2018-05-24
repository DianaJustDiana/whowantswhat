from django import forms
from .models import Offer, Dib

class OfferForm(forms.ModelForm):

    class Meta:
        model = Offer
        fields = ['description', 'photo']
        labels = {'description' : 'A brief description', 'photo': 'Add your photo'}

class DibForm(forms.ModelForm):

    class Meta:
        model = Dib
        fields = ['owner', 'offer']
