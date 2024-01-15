from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator,MinValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

GENRES_CHOICES = (
    ("Pop Music", "Pop Music"),
    ("Jazz Music", "Jazz Music"),
    ("R&B Music", "R&B Music"),
    ("Rock Music", "Rock Music"),
    ("Country Music", "Country Music"),
    ("Dance Music", "Dance Music"),
    ("Hip Hop Music", "Hip Hop Music"),
    ("Other", "Other"),
)

class Profile(models.Model):
    username = models.CharField(max_length=15, validators=[MinLengthValidator(limit_value=2),RegexValidator(
                regex=r'^[a-zA-Z0-9_]+$',
                message="Ensure this value contains only letters, numbers, and underscore.",
            )
        ])
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])


class Album(models.Model):
    album_name = models.CharField(max_length=150,unique=True)
    artist = models.CharField(max_length=30)
    genre = models.CharField(max_length = 30, choices=GENRES_CHOICES)
    description = models.TextField(blank=True)
    image_url = models.URLField(max_length=200)
    price = models.FloatField(validators=[MinValueValidator(0)])
