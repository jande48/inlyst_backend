from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import CustomUserManager
from django.db import models
from django.db.models import (
    CharField,
    EmailField,
    BooleanField,
    DateTimeField,
    ManyToManyField,
    ForeignKey,
    CASCADE
)
from customer.utils import get_current_date


class BaseUser(AbstractBaseUser, PermissionsMixin):
    objects = CustomUserManager()
    first_name = CharField("First Name", max_length=255, null=True, blank=True)
    last_name = CharField("Last Name", max_length=255, null=True, blank=True)
    phone_number = CharField(max_length=255, null=True, blank=True)
    email = EmailField(("Email"), unique=True, null=True, blank=True)
    is_staff = BooleanField(default=False)
    is_superuser = BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.first_name:
            return self.first_name
        else:
            return "No Name"


class Device(models.Model):
    created_at = DateTimeField(auto_now_add=True, null=True, blank=True)
    is_test = BooleanField(default=False)
    device_id = CharField(max_length=255, null=True, blank=True)

    def save(
        self,
        *args,
        **kwargs,
    ):
        if not self.created_at:
            self.created_at = get_current_date()
        super(Device, self).save(*args, **kwargs)


class Customer(BaseUser):
    created_at = DateTimeField(auto_now_add=True, null=True, blank=True)
    is_test = BooleanField(default=False)
    devices = ManyToManyField(to="customer.Device")
    verified_phone = DateTimeField(null=True, blank=True)

    def save(
        self,
        *args,
        **kwargs,
    ):
        if not self.created_at:
            self.created_at = get_current_date()
        super(Customer, self).save(*args, **kwargs)


class Employee(BaseUser):
    created_at = DateTimeField(auto_now_add=True, null=True, blank=True)

    def save(
        self,
        *args,
        **kwargs,
    ):
        if not self.created_at:
            self.created_at = get_current_date()
        super(Employee, self).save(*args, **kwargs)


class Credentials(models.Model):
    created_at = DateTimeField(auto_now_add=True, null=True, blank=True)
    name = CharField(max_length=255, null=True, blank=True)
    api_key = CharField(max_length=255, null=True, blank=True)

    def save(
        self,
        *args,
        **kwargs,
    ):
        if not self.created_at:
            self.created_at = get_current_date()
        super(Credentials, self).save(*args, **kwargs)

class VerificationCode(models.Model):
    created_at = DateTimeField(auto_now_add=True, null=True, blank=True)
    code = CharField(max_length=255, null=True, blank=True)
    customer = ForeignKey(
        Customer, on_delete=CASCADE, related_name="verification_code", null=True
    )

    def save(
        self,
        *args,
        **kwargs,
    ):
        if not self.created_at:
            self.created_at = get_current_date()
        super(VerificationCode, self).save(*args, **kwargs)
