from django import forms
from .models import Offer, Dib

class OfferForm(forms.ModelForm):

    class Meta:
        model = Offer
        
        fields = ['family', 'description', 'photo']
        labels = {'family': 'Choose which family', 'description': 'A brief description', 'photo': 'Add your photo'}

class DibForm(forms.ModelForm):

    class Meta:
        model = Dib
        fields = ['offer']
        #widgets = {'owner': forms.HiddenInput(), 'offer': forms.HiddenInput()} 