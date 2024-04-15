from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm  


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

def profile_details(request):
    pass

def profile_edit(request):
    pass

def profile_delete(request):
    pass