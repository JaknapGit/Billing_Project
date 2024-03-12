from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    ROLES = (
        ('owner', 'owner'),
        ('salesman', 'salesman'),
        ('staff', 'staff'),
        ('manager', 'manager')
    )
    address = models.TextField(blank=True)
    contact = PhoneNumberField(region='IN', blank=True)
    city = models.CharField(max_length=30, blank=True)
    pincode = models.CharField(max_length=6, blank=True)
    role = models.CharField(max_length=20, default='', blank=True, choices=ROLES)

    REQUIRED_FIELDS = ('email',)
    objects = UserManager()
