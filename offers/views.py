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
    #This is a queryset that grabs all the objects from the Offer table.
    #offers = Offer.objects.all()
    
    #This queryset grabs only the objects where the owner is the current user.
    current_user = request.user
    ##offers = Offer.objects.filter(owner=current_user)
    #TODO Use this later when changing template to show choice of family groups.
    ##this_family = Family.objects.filter(parent=current_user)

    ##print("This family:")
    ##print(this_family)
    
    offers = Offer.objects.filter(family__parent=current_user)
    ##print(this_family)
    print(offers)


    #TODO This works if current user has just one family group. Might break if more than one family group.
    title = "Stuff I'm offering  " #+ current_user.family.family_name
    
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
    print("This user's families:")
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
            #print(form.family)
            #Then save again for real.
            form.save()
            #print(form.family)
            #After user adds new offer, redirect user to offers index page.
            return HttpResponseRedirect(reverse('offers:index'))
    current_user = request.user

    context = {'form': form}
    return render(request, 'offers/new_offer.html', context)

@login_required(login_url='/')
def available_to_me(request):
    """Displays index of offers user can call dibs on."""
    #This is a queryset that grabs all the objects from the Offer table.
    #offers = Offer.objects.all()
    
    #This queryset grabs only the objects where the member is the current user.
    current_user = request.user
    print(current_user)
    offers = Offer.objects.filter(family=current_user.family)
    #offers = Offer.objects.filter(family__member=current_user)
    print(offers)


    #offers = Offer.objects.filter(owner=current_user)
    #TODO Use this later when changing template to show choice of family groups.
    #this_family = Family.objects.filter(parent=current_user)

    
    #offers = None
    #offers = Offer.objects.filter(family=all_the_families)

    #first_level = Family.objects.filter(member=current_user.id)
    #second_level = Offer.objects.filter(family=first_level)
    #offers = Offer.objects.filter(family=current_user_families)  
    
    title = "Items " + current_user.family.parent.username + " is offering me"
    
    #Context is the dictionary of info that populates the offers/index template.
    context = {
        "title": title,
        "offers": offers,
    }

    return render(request, 'offers/index.html', context)