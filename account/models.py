from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from account import managers as a_managers
from account import validators as a_validators


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name=_('Email'), validators=[a_validators.validate_email])
    first_name = models.CharField(max_length=30, blank=True, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=30, blank=True, verbose_name=_('Last Name'))
    password = models.CharField(max_length=128, verbose_name=_('Password'), validators=[a_validators.validate_password])
    is_active = models.BooleanField(default=True, verbose_name=_('Active'))
    confirmation_code = models.CharField(max_length=6, blank=True, null=True)
    is_verified = models.BooleanField(default=False, verbose_name=_('Verified'))
    is_staff = models.BooleanField(default=False, verbose_name=_('Staff Status'))
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_('Date Joined'))

    objects = a_managers.UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.email

