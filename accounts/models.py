from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
    )

    phone_number = models.CharField(
        max_length=10,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"
