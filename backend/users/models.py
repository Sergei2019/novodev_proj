from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    first_name = models.CharField(_("Имя"), max_length=150)
    last_name = models.CharField(_("Фамилия"), max_length=150)
    email = models.EmailField(_("E-mail"), max_length=254, unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username", "first_name", "last_name")