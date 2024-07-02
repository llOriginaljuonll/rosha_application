from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    id: int
    email = models.EmailField("Email Address", unique=True, blank=False, null=False)
    first_name = None
    last_name = None
    is_judge = models.BooleanField("Judge Status", default=False, help_text="Designates whether the user can grades participants.")

    def __str__(self):
        return f'{self.username} No.{self.id}'