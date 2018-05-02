from django.db import models
#Not sure.
from django.contrib.auth.models import AbstractUser
#Not sure.
# Create your models here.

#A user can belong to many families.
class User(AbstractUser):
    #name = models.CharField(blank=True, max_length=255)
    email = models.EmailField(blank=True, max_length=254, verbose_name='email address')

    def __str__(self):
        return self.email
 

 #A family has many users(parent=False).
#A family contains one parent, or user(parent=True).
class Family(models.Model):
    """A group of users."""
    family_name = models.CharField(max_length=20)

    #This fixes plural form so it's 'families' instead of default 'familys.'
    class Meta:
        verbose_name_plural = "families"