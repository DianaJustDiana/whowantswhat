from django.shortcuts import render
#Need for new_offer redirect.
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Offer
from .forms import OfferForm

# Create your views here.
#Should be a GET request. That's the default, so no need to specify.
def index(request):
    """Home page for Mysite. Will display index of offers."""
    offers = Offer.objects.all()
    #Context is the dictionary of info that populates the offers/index template.
    context = {
        "title": "All the offers",
        "offers": offers,
    }

    return render(request, 'offers/index.html', context)
    
#Works with POST or other (usually that means GET).
def new_offer(request):
    """User can add a new offer."""
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = OfferForm()
    else:
        #POST data submitted; process data.
        form = OfferForm(data=request.POST)
        if form.is_valid():
            form.save()
            #TODO check the offers:offers
            #After user addes new offer, redirect user to offers index page.
            return HttpResponseRedirect(reverse('offers:index'))

    context = {'form': form}
    return render(request, 'offers/new_offer.html', context)
