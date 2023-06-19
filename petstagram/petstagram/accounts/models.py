from django.contrib.auth import models as auth_models
from django.contrib.auth.models import User, UserManager
from django.db import models

from accounts.manager import PetStagramUserManager


# Create your models here.

class PetStagramUser(auth_models.AbstractBaseUser,auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH=30
    username = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=USERNAME_MAX_LENGTH
    )
    is_staff = models.BooleanField(
        default=False
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    USERNAME_FIELD = 'username'
    objects = PetStagramUserManager()
