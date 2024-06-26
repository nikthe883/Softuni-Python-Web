# Generated by Django 5.0.1 on 2024-04-15 15:43

import django.core.validators
import fruits.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='First name must be between 2 and 25 characters long and start with a letter.', max_length=25, validators=[fruits.models.validate_name_starts_with_letter, django.core.validators.MinLengthValidator(2)])),
                ('last_name', models.CharField(help_text='Last name must be between 1 and 35 characters long and start with a letter.', max_length=35, validators=[fruits.models.validate_name_starts_with_letter, django.core.validators.MinLengthValidator(1)])),
                ('email', models.EmailField(help_text='Email must be unique and no longer than 40 characters.', max_length=40, unique=True)),
                ('password', models.CharField(help_text='*Password length requirements: 8 to 20 characters', max_length=20, validators=[django.core.validators.MinLengthValidator(8)])),
                ('image_url', models.URLField(blank=True, help_text='Optional field for an image URL.', null=True)),
                ('age', models.IntegerField(blank=True, default=18, help_text='Optional age field with default value 18.', null=True)),
            ],
        ),
    ]
