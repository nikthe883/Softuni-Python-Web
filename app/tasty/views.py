from django.shortcuts import render, redirect
from .models import Profile, Recipe
from .forms import ProfileForm, RecipeForm, ProfileFormEdit
from .utils import get_recipe_by_id, get_first_profile, get_all_recipe

def home(request):
     profile = get_first_profile()

     return render(request, 'home-page.html', {"profile": profile})

def recipe_catalogue(request):
    recipe = get_all_recipe()
    profile = get_first_profile()

    return render(request,'catalogue.html', {'recipe': recipe, "profile": profile})

def recipe_create(request):
    profile = get_first_profile()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_catalogue')  
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = RecipeForm()

    return render(request, 'create-recipe.html', {'form': form, 'profile':profile})

def recipe_details(request,recipe_id):
    profile = get_first_profile()
    recipe = get_recipe_by_id(recipe_id)



    ingredients = recipe.ingredients.split(',')
    

    return render(request, 'details-recipe.html', {'recipe': recipe, 'profile':profile, 'ingredients': ingredients})

def recipe_edit(request,recipe_id):
    profile = get_first_profile()
    recipe = get_recipe_by_id(recipe_id)

    if request.method == 'POST':
        form = RecipeForm(request.POST,instance=recipe)
        if form.is_valid():
            
            form.save()
            
            return redirect('recipe_catalogue')  
        else:
            print("Form is not valid")
            print(form.errors)
    else:
       
        form = RecipeForm(instance=recipe)


    return render(request, 'edit-recipe.html', {'form': form, 'profile':profile})

def recipe_delete(request,recipe_id):
    profile = get_first_profile()
    recipe = get_recipe_by_id(recipe_id)

    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_catalogue')
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'delete-recipe.html', {'form': form, 'profile':profile})

def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()  
            print("Profile created")
            return redirect('recipe_catalogue')  
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = ProfileForm()

    return render(request, 'create-profile.html', {'form': form})

def profile_details(request):
    profile = get_first_profile()
    recipe_count = get_all_recipe().count()
    


    return render(request, 'details-profile.html', {'profile': profile,'recipe_count': recipe_count})

def profile_edit(request):
    profile = get_first_profile()
    
    if request.method == 'POST':
        form = ProfileFormEdit(request.POST,instance=profile)
        if form.is_valid():
            form.save()  
            
            return redirect('profile_details')  
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = ProfileFormEdit(instance=profile)


    return render(request, 'edit-profile.html', {'form': form,'profile': profile})

def profile_delete(request):
    profile = get_first_profile()
    recipe = get_all_recipe()

    if request.method == 'POST':
        profile.delete()
        recipe.delete()
        return redirect('home')
    return render(request, 'delete-profile.html', {'profile': profile})
