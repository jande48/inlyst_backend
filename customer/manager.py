from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from . import models


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        u = models.BaseUser(
            is_superuser=True,
            first_name="Root",
            email=email,
            phone_number="000",
            is_staff=True,
        )
        u.set_password(password)
        u.save()

        return u
