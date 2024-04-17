from django.shortcuts import get_object_or_404
from .models import Profile, Recipe

def get_first_profile():
    """ Utility function to fetch the first profile """
    return Profile.objects.first()

def get_recipe_by_id(recipe_id):
    """ Utility function to fetch a recipe by its ID """
    return get_object_or_404(Recipe, id=recipe_id)


def get_all_recipe():
    """ Utility function to fetch all recipes """
    return Recipe.objects.all()