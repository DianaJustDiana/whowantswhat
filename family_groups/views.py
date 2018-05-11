from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import CreateAFamilyForm, AddMembersForm

# Create your views here.
def create_a_family(request):
    """User can create a family group."""
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = CreateAFamilyForm()
    else:
        #POST data submitted; process data.
        form = CreateAFamilyForm(request.POST)

        if form.is_valid():
            #Saving the form with commit=False generates an object called "form."
            form = form.save(commit=False)       
            #Here's where I can add extra data and make the object's parent the current user. 
            form.parent = request.user
            #Then save again for real.
            form.save()
            #After user addes new offer, redirect user to offers index page.
            return HttpResponseRedirect(reverse('offers:index'))

    context = {'form': form}
    return render(request, 'family_groups/create_a_family.html', context) 

def add_members(request):
    """Parent of family group can add members."""
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = AddMembersForm()
    else:
        form = AddMembersForm(request.POST)

        if form.is_valid():
             #Saving the form with commit=False generates an object called "form."
            #form = form.save(commit=False)    
            #Here's where I can add extra data and make the object belong to the family group.
            #form.family = request.user. 
            form=form.save()
            #After user addes new offer, redirect user to offers index page.
            return HttpResponseRedirect(reverse('offers:index'))
    
    context = {'form': form}
    return render(request, 'family_groups/add_members.html', context) 