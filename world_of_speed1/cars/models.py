from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from world_of_speed1.cars.custom_validators import validate_year
from world_of_speed1.profiles.models import Profile


class Car(models.Model):
    class CarType(models.TextChoices):
        RALLY = "Rally"
        OPEN_WHEEL = "Open-wheel"
        KART = "Kart"
        DRAG = "Drag"
        OTHER = "Other"

    TYPE_MAX_LENGTH = 10
    MODEL_MAX_LENGTH = 15
    MODEL_MIN_LENGTH = 1
    PRICE_MIN_VALUE = 1.0

    type = models.CharField(
        max_length=TYPE_MAX_LENGTH,
        choices=CarType.choices,
        null=False,
        blank=False,
    )

    model = models.CharField(
        max_length=MODEL_MAX_LENGTH,
        validators=[
            MinLengthValidator(MODEL_MIN_LENGTH),
        ],
        null=False,
        blank=False,
    )

    year = models.IntegerField(
        validators=[
            validate_year,
        ],
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        unique=True,
        null=False,
        blank=False,
    )

    price = models.FloatField(
        validators=[
            MinValueValidator(
                PRICE_MIN_VALUE
            )
        ]
    )

    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
    )

