from django import forms
from .models import Offer

class OfferForm(forms.ModelForm):

    class Meta:
        model = Offer
        fields = ['description', 'photo', 'owner']
        labels = {'description' : 'A brief description', 'photo': 'Add your photo', 'owner': ''}