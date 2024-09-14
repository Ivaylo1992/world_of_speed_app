from django.core.exceptions import ValidationError


def validate_year(value):
    year_max_value = 2030
    year_min_value = 1999

    if value not in range(year_min_value, year_max_value + 1):
        raise ValidationError("Year must be between 1999 and 2030!")
