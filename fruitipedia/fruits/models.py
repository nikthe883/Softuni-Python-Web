from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.db import models

def validate_name_starts_with_letter(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")

class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=[
            validate_name_starts_with_letter,
            MinLengthValidator(2)
        ],
        help_text="First name must be between 2 and 25 characters long and start with a letter."
    )
    last_name = models.CharField(
        max_length=35,
        validators=[
            validate_name_starts_with_letter,
            MinLengthValidator(1)
        ],
        help_text="Last name must be between 1 and 35 characters long and start with a letter."
    )
    email = models.EmailField(
        max_length=40,
        unique=True,
        help_text="Email must be unique and no longer than 40 characters."
    )
    password = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(8)
        ],
        help_text="*Password length requirements: 8 to 20 characters"
    )
    image_url = models.URLField(
        blank=True,
        null=True,
        help_text="Optional field for an image URL."
    )
    age = models.IntegerField(
        default=18,
        blank=True,
        null=True,
        help_text="Optional age field with default value 18."
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
