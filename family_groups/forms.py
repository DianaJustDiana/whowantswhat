from django import forms
from .models import Family, Member
##Not sure if I need these, but let's try something.
##from django.forms import ModelChoiceField, ModelForm

class CreateAFamilyForm(forms.ModelForm):

    class Meta:
        model = Family
        fields = ['family_name']
        labels = {'family_name' : 'What you will call your family group'}

class AddMembersForm(forms.ModelForm):

    #my_family_groups = Family.objects.filter(parent=current_user)#.values('member__name__username', 'family_name', 'parent__username')
    #print("my family group(s)")
    #print(my_family_groups)

    ##family = forms.ModelChoiceField(widget=forms.Select(), queryset=Family.objects.all())
    
            #widget=forms.Select(), label="Choose which family:")
    class Meta:
        model = Member
        #TODO Need to limit family choices to those where parent = current user.
        fields = ['family', 'name']
        labels = {'family': 'choose which family', 'name' : 'add a person by email address'}

    
    ##def __init__(self, current_user, *args, **kwargs):
        #current_user = kwargs.pop('current_user')
    ##    super(AddMembersForm, self).__init__(*args, **kwargs)
        #Limit the family options to the ones owned by the current user.
    ##    self.fields['family'].choices = Family.objects.filter(parent=current_user)
                #Still working on how to handle member names.
      ##  self.fields['name'].queryset=Member.objects.all()
        #member_name = models.ForeignKey(User, on_delete=models.CASCADE)
    ##print("this is the list of family choices:")
    ##print(family)
