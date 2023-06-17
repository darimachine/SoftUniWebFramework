
from django.contrib.auth import models as  auth_models
from django.db import models

from auth_app.managers import AppUserManager


class AppUser(auth_models.AbstractBaseUser,auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False
    )
    is_staff = models.BooleanField(
        default=False
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    USERNAME_FIELD='email'
    objects = AppUserManager()

class Profile(models.Model):

    first_name=models.CharField(
        max_length=50,
    )
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )