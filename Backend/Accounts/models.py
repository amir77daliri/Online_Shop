from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
        extend AbstractBaseUser for using phone_number As username
    """
    phone_number = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=255, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=300, blank=True, null=True)
    last_name = models.CharField(max_length=300, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'

    @property
    def is_staff(self):
        return self.is_admin

    def get_fullname(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        return self.get_username()
