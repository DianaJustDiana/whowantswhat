from django.contrib import admin


# Register your models here.
#My app is called offers and the main model inside it is Offer.
from offers.models import Offer, Family, Dib, DibComment
admin.site.register(Offer)
admin.site.register(Family)
admin.site.register(Dib)
admin.site.register(DibComment)

from accounts.models import User
admin.site.register(User)