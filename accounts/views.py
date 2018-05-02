from django.shortcuts import render
#from django.contrib.auth.forms import UserCreationForm
#Import my version of the form instead of the default one.
from accounts.forms import MyUserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
class SignUp(generic.CreateView):
    #Also here -- need to use my version of the form instead of the default one.
    form_class = MyUserCreationForm
    #Redirects user to the login page after registering. TODO Might change this later.
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
