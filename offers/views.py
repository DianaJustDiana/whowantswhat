from django.shortcuts import render
#Need for new_offer redirect.
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Offer, User
from .forms import OfferForm

#Need for @login required decorator.
from django.contrib.auth.decorators import login_required

# Create your views here.
#Should be a GET request. That's the default, so no need to specify.
#@login_required sends unvalidated users to url of my choosing. In this case, the home page.
@login_required(login_url='/')
def index(request):
    """Home page for Mysite. Will display index of offers."""
    #This is a queryset that grabs all the objects from the Offer table.
    #offers = Offer.objects.all()
    
    #This queryset grabs only the objects where the owner is the current user.
    current_user = request.user
    offers = Offer.objects.filter(owner=current_user)
    
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
            form.family = request.user.family
            print(form.family)
            #Then save again for real.
            form.save()
            print(form.family)
            #After user adds new offer, redirect user to offers index page.
            return HttpResponseRedirect(reverse('offers:index'))
    current_user = request.user

    context = {'form': form}
    return render(request, 'offers/new_offer.html', context)


