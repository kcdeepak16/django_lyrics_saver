from django.shortcuts import render
from django import forms
from .models import *

# Create your views here.

class LyricsForm(forms.ModelForm):
    song_name = forms.CharField(max_length=100, label = "Song/Poem Name(Write 'Quote' for Quotes)")
    song_artist = forms.CharField(max_length=100, label = "Artist/Author Name")
    song_lyrics = forms.CharField(widget=forms.Textarea, label="Song Lyrics/Poem/Quote")
    song_image_url = forms.URLField(label="Image URL", required=False)
    language = forms.ChoiceField(choices=(('Hindi', 'Hindi'), ('English', 'English')), label="Language")
    type = forms.ChoiceField(choices=(('Song Lyrics', 'Song Lyrics'), ('Poetry', 'Poetry'), ('Quote', 'Quote')), label="Type")
    tags = forms.CharField(required=False)

    class Meta:
        model = lyrics
        fields = ['user','song_name', 'song_artist', 'song_lyrics', 'song_image_url', 'language', 'type', 'tags']

def home_page(request):
    all_lyrics = lyrics.objects.all()
    return render(request, 'home_page.html', {'all_lyrics': all_lyrics})

def add_lyric(request):
    if request.method == "POST":
        lyrics_form_sub = LyricsForm(request.POST)
        if lyrics_form_sub.is_valid():
            lyrics_form_sub.save()
        else:
            print(lyrics_form_sub.errors)
    lyric_form = LyricsForm(initial={'user': request.user.id, 'language': "English", "type": "Song Lyrics"})
    return render(request, 'add_lyric.html', {'lyric_form' : lyric_form})

def full_lyric(request, pk):
    fl = lyrics.objects.get(id=pk)
    return render(request, 'full_lyric.html', {'fl':fl})