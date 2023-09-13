# std-lib
import uuid
# Django
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.utils.translation import gettext_lazy as _
# Local
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Overriding email field
    email = models.EmailField(_("email address"), blank=False, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
