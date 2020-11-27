from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Playlist(models.Model):
    playlist_text=models.TextField()
    def __str__(self):
        return self.playlist_text

class Music(models.Model):
    playlist=models.ForeignKey(Playlist, on_delete=models.CASCADE, null=True)
    music_name=models.CharField(max_length=100)
    music_artist=models.CharField(max_length=100)
    url = models.FileField(upload_to ="playlist/music",blank = True, null =True)
    def __str__(self):
        return self.music_name