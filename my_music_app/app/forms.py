from django import forms
from .models import Profile, Album

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
 

class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'