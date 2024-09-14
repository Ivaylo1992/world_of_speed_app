from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from world_of_speed1.profiles.custom_validators import validate_username


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 25
    LAST_NAME_MAX_LENGTH = 25
    USERNAME_MAX_LENGTH = 15
    USERNAME_MIN_LENGTH = 3
    USER_MIN_AGE = 21
    PASSWORD_MAX_LENGTH = 20

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(
                USERNAME_MIN_LENGTH,
                message="Username must be at least 3 chars long!"
            ),
            validate_username
        ],
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.SmallIntegerField(
        validators=[
            MinValueValidator(
                USER_MIN_AGE,
                message="Age requirement: 21 years and above."
            )],
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=PASSWORD_MAX_LENGTH,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def get_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name or self.last_name:
            return self.first_name or self.last_name
        else:
            return self.username