from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models

from apps.users.managers import CustomUserManager
from apps.users.validators import validate_phone_number


class CustomUser(AbstractUser):
    username = None
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'phone_number'
    objects = CustomUserManager()

    phone_number = models.CharField(max_length=13, unique=True, validators=[validate_phone_number])
    email = models.EmailField()

    region = models.CharField(max_length=255)
    district = models.CharField(max_length=255)

    balance = models.DecimalField(max_digits=20, decimal_places=1, validators=[MinValueValidator(0)],
                                  help_text='IN UZS SUM', default=0)

    def __str__(self):
        return self.phone_number
