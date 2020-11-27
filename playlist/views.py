from django.views import generic
from django.shortcuts import render, reverse, get_object_or_404

from django.utils.decorators import method_decorator
from django.contrib.auth import views, models, login, decorators
from django.contrib.auth.decorators import login_required

from .forms import MusicForm, PlaylistForm
from django.urls import reverse_lazy
from playlist.models import Playlist, Music

from django.views.generic.base import View, TemplateResponseMixin
from django.views.generic.edit import FormMixin, ProcessFormView
# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse


class PlaylistListView(generic.ListView):
    model = Playlist
    context_object_name = 'playlist'
    template_name = 'playlist_final/playlist_list.html'
    def get_queryset(self):
        return Playlist.objects.order_by('playlist_text')[:10]

class PlaylistCreateView(generic.CreateView):
    model = Playlist
    fields = ['playlist_text']
    success_url = reverse_lazy('playlist:index')
    template_name = 'playlist_final/playlist_form.html'


class PlaylistUpdateView(generic.UpdateView):
    model = Playlist
    fields = ['playlist_text']
    success_url = reverse_lazy('playlist:index')
    template_name = 'playlist_final/playlist_form.html'


class PlaylistDeleteView(generic.DeleteView):
    model = Playlist
    success_url = reverse_lazy('playlist:index')
    template_name = 'playlist_final/playlist_confirm_delete.html'


class MusicDetailView(generic.DetailView):
    model = Playlist
    context_object_name = 'playlist'
    template_name = 'playlist_final/music_list.html'

class MusicCreateView(generic.CreateView):
    form_class =MusicForm
    template_name = 'playlist_final/music_form.html'
    success_url = reverse_lazy('playlist:index')

class MusicUpdateView(generic.UpdateView):
    model = Music
    template_name = 'playlist_final/music_form.html'
    fields = ['music_name','music_artist','url']
    success_url = reverse_lazy('playlist:index')

class MusicDeleteView(generic.DeleteView):
    model = Music
    template_name ='playlist_final/music_confirm_delete.html'
    success_url = reverse_lazy('playlist:index')