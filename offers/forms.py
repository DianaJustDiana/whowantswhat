from django import forms
from .models import Offer, Dib, Family


class OfferForm(forms.ModelForm):

    class Meta:
        model = Offer

        fields = ['family', 'description', 'photo']
        labels = {'family': 'Choose which family',
                  'description': 'A brief description', 'photo': 'Add your photo'}

    # This section limits dropdown options to stuff owned by the current user.
    def __init__(self, request, *args, **kwargs):
        super(OfferForm, self).__init__(*args, **kwargs)
        queryset = Family.objects.filter(parent=request)
        self.fields['family'].queryset = queryset


class DibForm(forms.ModelForm):

    class Meta:
        model = Dib
        fields = ['offer']
        #widgets = {'owner': forms.HiddenInput(), 'offer': forms.HiddenInput()}
