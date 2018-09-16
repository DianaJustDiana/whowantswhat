from django import forms
from .models import Family, Member
# Not sure if I need these, but let's try something.
##from django.forms import ModelChoiceField, ModelForm


class CreateAFamilyForm(forms.ModelForm):

    class Meta:
        model = Family
        fields = ['family_name']
        labels = {'family_name': 'What you will call your family group'}


class AddMembersForm(forms.ModelForm):

    class Meta:
        model = Member
        ##fields = "__all__"
        # TODO Need to limit family choices to those where parent = current user.
        fields = ['family', 'name']
        ##labels = {'family': 'choose which family', 'name' : 'add a person by email address'}

    # This section limits dropdown options to stuff owned by the current user.
    def __init__(self, current_user, *args, **kwargs):
        super(AddMembersForm, self).__init__(*args, **kwargs)
        my_queryset = Family.objects.filter(parent=current_user)
        self.fields['family'].queryset = my_queryset

        # Still working on how to handle member names.
        ##self.fields['name'].queryset = Member.objects.all()
        ##member_name = models.ForeignKey(User, on_delete=models.CASCADE)
    ##print("this is the list of family choices:")
    # print(family)

    # start trying something different
    # family = forms.ModelChoiceField(
    # widget=forms.Select, queryset=Family.objects.none())
    ##family = forms.ModelChoiceField(widget=forms.Select, queryset=Family.objects.filter(parent=current_user))

    ##name = forms.ModelChoiceField(queryset=Member.objects.all())
    # end trying something different

    # my_family_groups = Family.objects.filter(parent=current_user)#.values('member__name__username', 'family_name', 'parent__username')
    #print("my family group(s)")
    # print(my_family_groups)

    ##family = forms.ModelChoiceField(widget=forms.Select(), queryset=Family.objects.all())

    # widget=forms.Select(), label="Choose which family:")
