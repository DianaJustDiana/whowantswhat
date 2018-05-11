from django import forms
from .models import Family

class CreateAFamilyForm(forms.ModelForm):

    class Meta:
        model = Family
        fields = ['family_name']
        labels = {'family_name' : 'What you will call your family group'}