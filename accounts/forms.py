from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#Need the next two lines because my User is actually accounts.User.
from django.contrib.auth import get_user_model
User = get_user_model()

#This is where to add extra fields to the user signup form.
#I added "email" to the form. Didn't need to add it to the user model because the
#native user model already includes that.
class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        #This is where I specified the fields the user will see on the signup form.
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(MyUserCreationForm, self).save(commit=False)
        #Because I added this to the form it didn't go through "is_valid."
        #So I need to put it through the "cleaned_data" attribute before saving..
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user