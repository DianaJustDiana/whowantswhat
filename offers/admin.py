from django.contrib import admin

# Register your models here.
#My app is called offers and the main model inside it is Offer.
from offers.models import Offer
admin.site.register(Offer)

#from offers.models import User
#admin.site.register(User)

from offers.models import Family
admin.site.register(Family)

from offers.models import Dib
admin.site.register(Dib)

from offers.models import DibComment
admin.site.register(DibComment)
