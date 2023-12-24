from django.db import models
from django.contrib.auth.models import User
import string
# Create your models here.


class lyrics(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    song_name=models.CharField(max_length=100)
    song_artist=models.CharField(max_length=100)
    song_lyrics=models.TextField()
    song_image_url=models.URLField(blank=True)
    language=models.CharField(choices=(('Hindi', 'Hindi'), ('English', 'English')), max_length=10, default="English")
    type=models.CharField(choices=(('Song Lyrics', 'Song Lyrics'), ('Poetry', 'Poetry'), ('Quote', 'Quote')), max_length=20, default="Song Lyrics")
    tags=models.CharField(max_length=100, blank=True)

    def get_class_list(self):
        type_dict = {"Song Lyrics": "song_lyric", "Poetry": "poetry", "Quote": "quote"}
        return type_dict[self.type] + " " + self.language.lower()

    def __str__(self):
        return self.song_name

    def save(self, *args, **kwargs):
        self.song_name = string.capwords(self.song_name)
        self.song_artist = string.capwords(self.song_artist)
        self.song_lyrics = self.song_lyrics.replace("\n", "<br>")
        super(lyrics, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural="Lyrics"