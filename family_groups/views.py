from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import JoinAFamilyForm

# Create your views here.
def join_a_family_group(request):
    """User can join a family group."""
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = JoinAFamilyForm()
    else:
        #POST data submitted; process data.
        form = JoinAFamilyForm(request.POST)

        if form.is_valid():
            form.save()
            #Saving the form with commit=False generates an object called "form."
            #form = form.save(commit=False)       
            #Here's where I can add extra data and make the object's owner the current user. 
            #form.owner = request.user
            #Then save again for real.
            #form.save()
            #After user addes new offer, redirect user to offers index page.
            return HttpResponseRedirect(reverse('offers:index'))

    context = {'form': form}
    return render(request, 'family_groups/join_a_family_group.html', context) 