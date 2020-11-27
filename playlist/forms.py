from django.forms import inlineformset_factory
from django import forms
from django.db import models
from .models import *
class MusicForm (forms.ModelForm):
    class Meta :
        model = Music
        fields =['playlist','music_name','music_artist','url']
class PlaylistForm(forms.ModelForm):
    class Meta:
        model =Playlist
        fields =['playlist_text']