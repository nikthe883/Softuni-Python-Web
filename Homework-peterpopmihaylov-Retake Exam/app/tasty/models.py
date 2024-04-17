from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

def validate_capital_letter(value):
    if not value[0].isupper():
        raise ValidationError("Name must start with a capital letter!")

class Profile(models.Model):
    nickname = models.CharField(
        max_length=20, unique=True, blank=False,
        validators=[MinLengthValidator(2, message="Nickname must be at least 2 chars long!")]
    )
    first_name = models.CharField(
        max_length=30, blank=False, validators=[validate_capital_letter]
    )
    last_name = models.CharField(
        max_length=30, blank=False, validators=[validate_capital_letter]
    )
    chef = models.BooleanField(default=False)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.nickname

class Recipe(models.Model):


    title = models.CharField(
        max_length=100, unique=True, blank=False,
        validators=[MinLengthValidator(10, message="Title must be at least 10 chars long!")]
    )
    CUISINE_CHOICES = [
        ('French', 'French'),
        ('Chinese', 'Chinese'),
        ('Italian', 'Italian'),
        ('Balkan', 'Balkan'),
        ('Other', 'Other'),
    ]
    cuisine_type = models.CharField(
        max_length=7, choices=CUISINE_CHOICES, blank=False
    )
    ingredients = models.TextField(
        blank=False,
        help_text="Ingredients must be separated by a comma and space."
    )
    instructions = models.TextField(blank=False)
    
    cooking_time = models.PositiveIntegerField(
        blank=False,
        validators=[MinValueValidator(1, message="Time cannot be below 1.")],
        help_text="Provide the cooking time in minutes."
    )
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.title

