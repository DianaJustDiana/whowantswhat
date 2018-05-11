from django.contrib import admin
from django.contrib.auth import get_user_model
User = get_user_model()


# Register your models here.
#My app is called offers and the main model inside it is Offer.
from .models import Offer
from accounts.models import User
#, Family


class OfferAdmin(admin.ModelAdmin):
    list_display = ('description', 'added_date', 'photo', 'owner', 'owner_id')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'id')

class FamilyGroupAdmin(admin.ModelAdmin):
    list_display = ()


admin.site.register(Offer, OfferAdmin)
admin.site.register(User, UserAdmin)
#admin.site.register(Family)


