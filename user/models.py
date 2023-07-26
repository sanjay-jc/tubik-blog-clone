from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import Custom_manager
# Create your models here.


class Custom_user(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


    objects = Custom_manager()

    def __str__(self):
        return self.email
