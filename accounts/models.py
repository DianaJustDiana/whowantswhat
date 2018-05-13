from django.db import models
#Not sure.
from django.contrib.auth.models import AbstractUser
#Not sure.
# Create your models here.

#A user belongs to a family.
class User(AbstractUser):
    #name = models.CharField(blank=True, max_length=255)
    email = models.EmailField(blank=True, max_length=254, verbose_name='email address')
    #TODO Ask Brian to look at this.
    is_parent = models.BooleanField(default=False)


    
##    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    #A user is not a parent unless they sign up to make offers. Then parent = True.
    #parent = False

    def __str__(self):
        return self.email
 
