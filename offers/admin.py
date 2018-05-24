from django.contrib import admin
from django.contrib.auth import get_user_model
User = get_user_model()


# Register your models here.
#My app is called offers and the main model inside it is Offer.
from .models import Offer, Dib
from accounts.models import User
from family_groups.models import Family, Member


class OfferAdmin(admin.ModelAdmin):
    list_display = ('description', 'added_date', 'photo', 'owner', 'owner_id', 'family')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'id')

class FamilyAdmin(admin.ModelAdmin):
    list_display = ('family_name', 'parent')

class MemberAdmin(admin.ModelAdmin):
    list_display = ('family', 'name')

class DibAdmin(admin.ModelAdmin):
    list_display = ('owner', 'offer')


admin.site.register(Offer, OfferAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Family, FamilyAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Dib, DibAdmin)


