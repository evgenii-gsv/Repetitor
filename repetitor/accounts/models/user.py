from typing import List

from django.contrib.auth.models import AbstractUser
from django.db import models

from ..managers import UserManager


class User(AbstractUser):

    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS: List[str] = []
