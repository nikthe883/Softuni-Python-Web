from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm, EditProfileForm


def index(request):
    profile = Profile.objects.all().first()
    
    return render(request, 'index.html', {"profile": profile})


def dashboard(request):
    profile = Profile.objects.all().first()
    return render(request, 'dashboard.html', {"profile": profile})

def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            form.save()
            
            return redirect('dashboard')  
        else:
            print("Form is not valid")
            print(form.errors)
    else:
       
        form = ProfileForm()
        
    return render(request, 'create-profile.html', {'form': form})

def details_profile(request):
    profile = Profile.objects.all().first()
    return render(request, 'details-profile.html', {"profile": profile})

def edit_profile(request):
    profile = Profile.objects.all().first()
    
    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance=profile)
        if form.is_valid():
            
            form.save()
            
            return redirect('details_profile')  
        else:
            print("Form is not valid")
            print(form.errors)
    else:
       
        form = EditProfileForm(instance=profile)
        
    return render(request, 'edit-profile.html', {'form': form,'profile': profile})

def delete_profile(request):
    profile = Profile.objects.all().first()
    if request.method == 'POST':
        profile.delete()
        return redirect('index')

    return render(request, 'delete-profile.html', {'profile': profile})