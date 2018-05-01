from django.db import models

# Create your models here.

#An offer belongs to a user(parent=True).
#An offer has many dibs.
class Offer(models.Model):
    """An offer made by a user."""
    description = models.CharField(max_length=200)
    added_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(default='not sure')
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-added_date',)

    """Return a string representation of the offer."""
    def __str__(self):
        return self.description

#A user has many offers.
#A user has many dibs.
#A user belongs to a family.
#class User(models.Model):
#    """About a user."""
#    user_name = models.CharField(max_length=20)
#    email = models.EmailField()
#    parent = models.BooleanField(default=False)
#    family = models.ForeignKey('Family', on_delete=models.CASCADE)
    #password = models.
    #avatar = models.ImageField()

#    """Return a string representation of the user."""
#    def __str__(self):
#        return self.user_name

#A family has many users(parent=False).
#A family contains one parent, or user(parent=True).
class Family(models.Model):
    """A group of users."""
    family_name = models.CharField(max_length=20)

    #This fixes plural form so it's 'families' instead of default 'familys.'
    class Meta:
        verbose_name_plural = "families"

#A dib belongs to a user (parent=False).
#A dib belongs to an offer? Maybe allow multiple users to call dibs but ordered by timestamp.
class Dib(models.Model):
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    offer = models.ForeignKey('Offer', on_delete=models.CASCADE)
    dib_time_stamp = models.DateTimeField(auto_now_add=True)

#A dibcomment belongs to a user (parent=False).
#A dibcomment belongs to an offer.
class DibComment(models.Model):
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    offer = models.ForeignKey('Offer', on_delete=models.CASCADE)
    dib_comment_time_stamp = models.DateTimeField(auto_now_add=True)
 
