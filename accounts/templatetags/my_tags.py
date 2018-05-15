from django import template

register = template.Library()

#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
#from ..models import User


#TODO Why doesn't this work? Already have is_parent as a boolean (default=False) when user registers.
#If flips to True when user creates a family group. Already checked via print statements seen in terminal.
@register.simple_tag(name='owns_a_family_group')
def owns_a_family_group(user):
    #return user.is_parent
    pass