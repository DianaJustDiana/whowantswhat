from django.shortcuts import render
#Need for new_offer redirect.
#from django.http import HttpResponseRedirect
#from django.urls import reverse
from django.shortcuts import redirect


from .models import Offer, User, Family, Dib
from .forms import OfferForm, DibForm

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
    offers = Offer.objects.filter(family__parent=current_user)#.values('description', 'photo', 'dib__owner__username')     
    
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
            return redirect('offers:index')      

    context = {'form': form}
    return render(request, 'offers/new_offer.html', context)

@login_required(login_url='/')
def available_to_me(request):
    """Displays index of offers user can call dibs on."""
    current_user = request.user

    offers = Offer.objects.filter(family__member__name=current_user)#.values('dib__owner__username', 'description', 'photo', 'owner__username', 'owner__family__family_name', 'id')
    
    title = "Items being offered to me" 
    
    #Context is the dictionary of info that populates the offers/index template.
    context = {
        "title": title,
        "offers": offers,
        "current_user": current_user,
    }

    return render(request, 'offers/available_to_me.html', context)


@login_required(login_url='/')
def add_dib(request):
    """Displays index of offers user can call dibs on."""
    current_user = request.user
    
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = DibForm()
    else:
        #POST data submitted; process data.
        form = DibForm(request.POST)

        if form.is_valid():

            #Saving the form with commit=False generates an object called "form."
            form = form.save(commit=False)       
            #Here's where I can add extra data and make the object's owner the current user. 
            form.owner = current_user
            
            #Already hid the dib button in cases where the current user is the offer owner. But just in case,
            #Let's add conditional here to prevent current user from calling dibs on own stuff.
            if form.offer.owner == form.owner:
                
                return redirect('offers:available_to_me')
            #Here's where I can make the dib associated with the current offer.
            #form.offer = offer.id
            #Then save again for real.
            else:
                form.save()
                #After user adds new offer, redirect user to offers index page.
                return redirect('offers:available_to_me')
        else:
            print("The form is not valid.")
            
    context = {'form': form}
    return render(request, 'offers/available_to_me.html', context)

@login_required(login_url='/')
def all_my_dibs(request):
  
    current_user = request.user
  
    my_dibs = Offer.objects.filter(dib__owner=current_user)#.values('description', 'photo')

    title = "Items I've called dibs on" 
    
    #Context is the dictionary of info that populates the offers/index template.
    context = {
        "title": title,
        "my_dibs": my_dibs,
    }

    return render(request, 'offers/all_my_dibs.html', context)


@login_required(login_url='/')
def dibs_on_my_stuff(request):
  
    current_user = request.user
    offers = Offer.objects.filter(family__parent=current_user)  
    title = "My items that people have called dibs on"
    
    #Context is the dictionary of info that populates the offers/index template.
    context = {
        "title": title,
        "offers": offers,
    }

    return render(request, 'offers/dibs_on_my_stuff.html', context)
         


