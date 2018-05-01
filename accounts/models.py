from django.db import models
#Not sure.
from django.contrib.auth.models import AbstractUser
#Not sure.
# Create your models here.
class User(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    email = models.EmailField(blank=True, max_length=254, verbose_name='email address')

    def __str__(self):
        return self.email
 