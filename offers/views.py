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
    offers = Offer.objects.filter(family__parent=current_user).values('dib__owner__username', 'description', 'photo')

    print("All the offers:")
    print(offers)



##SELECT Offers_Offer.description, Offers_Offer.photo, Offers_Dib.owner_id, Offers_Dib.id
##FROM Offers_Offer
##INNER JOIN Offers_Dib ON Offers_Offer.ID=Offers_Dib.Offer_ID

    #TODO This works if current user has just one family group. Might break if more than one family group.
    title = "Stuff I'm offering to " + current_user.family.family_name
    
    #Context is the dictionary of info that populates the offers/index template.
    context = {
        "title": title,
        "offers": offers,
        "current_user": current_user,
    }

    return render(request, 'offers/index.html', context)
    
#@login_required sends unvalidated users to url of my choosing. In this case, the home page.    
@login_required(login_url='/')    
#Works with POST or other (usually that means GET).
def new_offer(request):
    """User can add a new offer."""
    current_user = request.user
    print("First time:")
    print(current_user)
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
            #return HttpResponseRedirect(reverse('offers:index'))
            return redirect('offers:index')
    print("Second time:")
    print(current_user)        

    context = {'form': form}
    return render(request, 'offers/new_offer.html', context)

@login_required(login_url='/')
def available_to_me(request):
    """Displays index of offers user can call dibs on."""
    current_user = request.user
    print(current_user)


    offers = Offer.objects.filter(family__member__name=current_user).values('dib__owner__username', 'description', 'photo', 'owner__username', 'owner__family__family_name')

    #This queryset grabs only the objects where the member is the current user.
    #It grabs family objects that have a member with name field matching current user.
    #The double underscore is important!!
    ##my_family_groups = Family.objects.filter(member__name=current_user)
    
    ##print("User's family groups:")
    ##print(my_family_groups)

    #For testing:
    ##for each in my_family_groups:
    ##    print("My family:")
    ##    print(each)
    #This queryset grabs all offers available to each my_family. User might have more than one.
    ##offers = []    
    ##for each in my_family_groups:
    ##    offers += Offer.objects.filter(family=each)#.values('dib', 'description', 'photo')
    
    
    #For testing:
    print("My offers:")
    print(offers)
    


    #TODO Make better title that includes the name of the offering parent.
    title = "Items being offered to me" #+ current_user.family.parent.username + " is offering me"
    
    #Context is the dictionary of info that populates the offers/index template.
    context = {
        "title": title,
        "offers": offers,
        ##"my_family_groups": my_family_groups,
        #"dibs": dibs,
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
        print(form)

        if form.is_valid():

            #Saving the form with commit=False generates an object called "form."
            form = form.save(commit=False)       
            #Here's where I can add extra data and make the object's owner the current user. 
            form.owner = current_user
            print("The dib owner:")
            print(form.owner)
            print("the owner of this offer:")
            print(form.offer.owner)
            
            #Already hid the dib button in cases where the current user is the offer owner. But just in case,
            #Let's add conditional here to prevent current user from calling dibs on own stuff.
            if form.offer.owner == form.owner:
                
                return redirect('offers:available_to_me')
            #Here's where I can make the dib associated with the current offer.
            #form.offer = offer.id
            #print("The current offer:")
            #Then save again for real.
            else:
                form.save()
                #After user adds new offer, redirect user to offers index page.
                #return HttpResponseRedirect(reverse('offers:index'))
                return redirect('offers:available_to_me')
        else:
            print("The form is not valid.")
            
    context = {'form': form}
    return render(request, 'offers/index.html', context)

@login_required(login_url='/')
def all_my_dibs(request):
  
    current_user = request.user
  
    my_dibs = Offer.objects.filter(dib__owner=current_user)#.values('description', 'photo')
    print("Stuff I've called dibs on:")
    print(my_dibs)

    title = "Items I've called dibs on" #+ current_user.family.parent.username + " is offering me"
    
    #Context is the dictionary of info that populates the offers/index template.
    context = {
        "title": title,
        "my_dibs": my_dibs,
    }

    return render(request, 'offers/all_my_dibs.html', context)


@login_required(login_url='/')
def dibs_on_my_stuff(request):
  
    current_user = request.user
    current_family = Family.objects.get(parent=current_user)
    #print("The current family:")
    #print(current_family)

    my_dibs = Dib.objects.filter(offer__family=current_family)
    #print("My dibs:")
    #print(my_dibs)
    #for each in my_dibs:
    #    print(each.owner)
    #    print(each.offer)

    title = "My items that people have called dibs on" #+ current_user.family.parent.username + " is offering me"
    
    #Context is the dictionary of info that populates the offers/index template.
    context = {
        "title": title,
        "my_dibs": my_dibs,
    }

    return render(request, 'offers/dibs_on_my_stuff.html', context)
         


