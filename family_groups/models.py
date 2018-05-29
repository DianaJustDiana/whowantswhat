from django.db import models

#Need the next two lines because my User is actually accounts.User.
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

#A family has many users.
#A family contains one parent.
class Family(models.Model):
    """Has many family members."""
    family_name = models.CharField(max_length=200)
    parent = models.OneToOneField(User, on_delete=models.CASCADE)

    #This fixes plural form so it's 'families' instead of default 'familys.'
    class Meta:
        verbose_name_plural = "families"
    
    def __str__(self):
        return self.family_name

#A Member belongs to a Family.
class Member(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)