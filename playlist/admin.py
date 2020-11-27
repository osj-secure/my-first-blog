from django.contrib import admin
from playlist.models import Playlist,Music
# Register your models here.
class MusicInline(admin.TabularInline):
    model=Music
    extra=1
class PlaylistAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Playlist', {'fields': ['playlist_text'], 'classes': {'collapse'}})
    ]
    inlines=[MusicInline]
    list_display=('playlist_text',)
    search_fields=['playlist_text']
admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Music)

