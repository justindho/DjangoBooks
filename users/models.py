from django.contrib.auth.models import AbstractUser
from django.db import models

# https://wsvincent.com/django-custom-user-model-tutorial/
class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username
