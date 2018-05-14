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
        #TODO Need to limit family choices to those where parent = current user.
        fields = ['name']
        labels = {'name' : 'add a person by email address'}