from django import forms
from .models import Family, Member

class CreateAFamilyForm(forms.ModelForm):

    class Meta:
        model = Family
        fields = ['family_name']
        labels = {'family_name' : 'What you will call your family group'}

class AddMembersForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = ['family', 'member']
        labels = {'member' : 'add a person by email address'}