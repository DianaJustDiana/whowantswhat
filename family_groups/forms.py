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
        print("The model part worked.")
        ##fields = "__all__"
        # TODO Need to limit family choices to those where parent = current user.
        fields = ['family', 'name']
        ##labels = {'family': 'choose which family', 'name' : 'add a person by email address'}

    def __init__(self, current_user, *args, **kwargs):
        print("This is from the init")
        ##current_user = kwargs.pop('current_user')
        super(AddMembersForm, self).__init__(*args, **kwargs)
        print("This is also from the init")

        my_queryset = Family.objects.filter(parent=current_user)
        print("The current user is parent to these families:")
        print(my_queryset)
        # if request.user:
        ##    queryset = Family.objects.filter(parent=request.user)
        # else:
        ##    queryset = Family.objects.all()
        # Limit the family options to the ones owned by the current user.
        self.fields['family'].queryset = my_queryset
        print("my_queryset:")
        print(self.fields['family'].queryset)
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
