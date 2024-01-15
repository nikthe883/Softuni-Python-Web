from django.shortcuts import render, redirect
from .forms import CreateProfileForm, CreateAlbumForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Album


def home(request):
    
    profile = Profile.objects.all().first()
    
    if profile is None:
  
        form = CreateProfileForm()
        if request.method == 'POST':
            form = CreateProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("home")
        
        context = {'CreateProfileForm': form,
                   'profile':profile}

        return render(request,'home-no-profile.html',context)

    else:
        context = {
            'profile': profile,
            'albums': Album.objects.all(),
        }
        return render(request, 'home-with-profile.html', context=context)


def add_album(request):
    profile = Profile.objects.all().first()
    form = CreateAlbumForm()
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    
    context = {'CreateAlbumForm': form,
               'profile': profile}

    return render(request,'add-album.html',context)



def details_album(request,pk):
    profile = Profile.objects.all().first()
    try:
        album = Album.objects.get(id=pk)
    except:
        return redirect('create-album')

    context = {'UpdateAlbumForm': album,
               'profile': profile}
    
    return render(request, 'album-details.html',context)



def edit_album(request,pk):
    profile = Profile.objects.all().first()
    try:
        album = Album.objects.get(id=pk)
    except:
        return redirect('create-album')
    
    form = CreateAlbumForm(instance=album)
    if request.method == 'POST':
       
        form = CreateAlbumForm(request.POST,instance=album)
        if form.is_valid():
            form.save()
           
            return redirect('home')
        
    context = {'form' : form,
               'profile': profile}

    return render(request, 'edit-album.html', context)


def delete_album(request,pk):

    profile = Profile.objects.all().first()
    try:
        album = Album.objects.get(id=pk)
    except:
        return redirect('create-album')
    
    form = CreateAlbumForm(instance=album)
    if request.method == "POST":
        print("here")
        album.delete()

        return redirect('home')
    
    context = {'form' : form,
               'profile': profile}
    
    return render(request, 'delete-album.html', context)


def profile_details(request):
    profile = Profile.objects.all().first()
    album = Album.objects.all().count()
    context = {'profile': profile,
               "album": album}
    return render(request, 'profile-details.html',context)

def profile_delete(request):
     profile = Profile.objects.all().first()
     albums = Album.objects.all()
     print(profile)
     if request.method == 'POST':
         profile.delete()
         albums.delete()
         return redirect('home')
     return render(request, 'profile-delete.html')

