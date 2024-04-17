from django.forms import ModelForm
from django import forms
from .models import Profile, Recipe

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'first_name', 'last_name', 'chef']


class ProfileFormEdit(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'cuisine_type', 'ingredients', 'instructions', 'cooking_time', 'image_url']
        widgets = {
            'cuisine_type': forms.Select(),
            'ingredients': forms.Textarea(attrs={
                'placeholder': 'ingredient1, ingredient2, ...',
                'help_text': 'Ingredients must be separated by a comma and space.'
            }),
            'instructions': forms.Textarea(attrs={
                'placeholder': 'Enter detailed instructions here...'
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'Optional image URL here...'
            }),
            'cooking_time': forms.NumberInput(attrs={
                'help_text': 'Provide the cooking time in minutes.'
            })
        }


