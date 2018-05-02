from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#Need the next two lines because my User is actually accounts.User.
from django.contrib.auth import get_user_model
User = get_user_model()

class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(MyUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user