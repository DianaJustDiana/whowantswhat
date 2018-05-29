from django.db import models
#from accounts.models import User

#Need the next two lines because my User is actually accounts.User.
from django.contrib.auth import get_user_model
User = get_user_model()
from family_groups.models import Family

# Create your models here.

#An offer belongs to an owner(user).
#An offer has many dibs.
class Offer(models.Model):
    """An offer made by a user."""
    description = models.CharField(max_length=255)
    added_date = models.DateTimeField(auto_now_add=True)
    #TODO need to add default image.
    #Image will be uploaded to MEDIA_ROOT/offerpics/.
    photo = models.ImageField(upload_to='offerpics/', default='images/images-9.jpeg')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-added_date',)

    """Return a string representation of the offer."""
    def __str__(self):
        return self.description

#A dib belongs to an owner (user).
#A dib belongs to an offer? Maybe allow multiple users to call dibs but ordered by timestamp.
class Dib(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    dib_time_stamp = models.DateTimeField(auto_now_add=True)

#A dibcomment belongs to an owner(user).
#A dibcomment belongs to an offer.
class DibComment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    dib_comment_time_stamp = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=255)