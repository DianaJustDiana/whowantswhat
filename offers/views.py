from django.shortcuts import render
#Need for new_offer redirect.
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Offer, User, Family
from .forms import OfferForm

#Need for @login required decorator.
from django.contrib.auth.decorators import login_required

# Create your views here.
#Should be a GET request. That's the default, so no need to specify.
#@login_required sends unvalidated users to url of my choosing. In this case, the home page.
#TODO Need to add conditional so if there is no family, user's start screen is something else.
@login_required(login_url='/')
def index(request):
    """Displays index of offers created by user."""    
    current_user = request.user
    #This queryset grabs only the objects where the owner is the current user.
    offers = Offer.objects.filter(family__parent=current_user)
    print("All the offers:")
    print(offers)

    #TODO This works if current user has just one family group. Might break if more than one family group.
    title = "Stuff I'm offering to " + current_user.family.family_name
    
    #Context is the dictionary of info that populates the offers/index template.
    context = {
        "title": title,
        "offers": offers,
    }

    return render(request, 'offers/index.html', context)
    
#@login_required sends unvalidated users to url of my choosing. In this case, the home page.    
@login_required(login_url='/')    
#Works with POST or other (usually that means GET).
def new_offer(request):
    """User can add a new offer."""
    current_user = request.user

    this_family = Family.objects.get(parent=current_user)
    print("This user's family:")
    print(this_family)

    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = OfferForm()
    else:
        #POST data submitted; process data.
        #Two bits here -- request.POST for text, request.FILES for images.
        form = OfferForm(request.POST, request.FILES)

        if form.is_valid():
            
            #Saving the form with commit=False generates an object called "form."
            form = form.save(commit=False)       
            #Here's where I can add extra data and make the object's owner the current user. 
            form.owner = request.user
            #Here's where I can make the object's family the current user's family.
            form.family = this_family
            #Then save again for real.
            form.save()
            #After user adds new offer, redirect user to offers index page.
            return HttpResponseRedirect(reverse('offers:index'))
    current_user = request.user

    context = {'form': form}
    return render(request, 'offers/new_offer.html', context)

@login_required(login_url='/')
def available_to_me(request):
    """Displays index of offers user can call dibs on."""
    current_user = request.user
    print(current_user)
    #This queryset grabs only the objects where the member is the current user.
    #It grabs family objects that have a member with name field matching current user.
    #The double underscore is important!!
    my_family = Family.objects.get(member__name=current_user)
    print("My family:")
    print(my_family)
    #This queryset grabs all offers available to my_family.
    offers = Offer.objects.filter(family=my_family)
    print("My offers:")
    print(offers)
    
    #TODO Make better title that includes the name of the offering parent.
    title = "Items being offered to me" #+ current_user.family.parent.username + " is offering me"
    
    #Context is the dictionary of info that populates the offers/index template.
    context = {
        "title": title,
        "offers": offers,
    }

    return render(request, 'offers/index.html', context)