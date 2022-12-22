from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

class CustomUserManager(BaseUserManager):

    def create_user(self,email,password,**extraFields):
        if not email:
            raise ValueError(_('email should be provided'))

        email = self.normalize_email(email)

        new_user = self.model(email=email,**extraFields)
        new_user.set_password(password)
        new_user.save()

        return new_user

    def create_superuser(self,email,password,**extraFields):

        extraFields.setdefault('is_staff',True)
        extraFields.setdefault('is_superuser',True)
        extraFields.setdefault('is_active',True)

        if extraFields.get('is_staff') is not True:
            raise ValueError(_('Superuser should have is_staff true'))

        if extraFields.get('is_superuser') is not True:
            raise ValueError(_('Superuser should have is_superuser true'))

        if extraFields.get('is_active') is not True:
            raise ValueError(_('Superuser should have is_active true'))

        return self.create_user(email,password,**extraFields)
