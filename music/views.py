from django.views.generic import CreateView, ListView, DetailView
from .models import Song, Album, Cover, Genre, Author, Country, City
from django.shortcuts import (
    render,
    redirect ,
    get_object_or_404 
)


class SongListView(ListView):
    model = Song


class AlbumListView(ListView):
    model = Album


class AlbumDetailView(DetailView):
    model = Album


class PlaySong(DetailView):
    model = Song


class SongCreateView(CreateView):
    model = Song
    fields = ['title', 'author', 'audio', 'cover', 'duration', 'lyric', 'rating']
    success_url = '/music/albums'


class AlbumCreaeView(CreateView):
    model = Album
    fields = ['songs', 'title', 'cover', 'author', 'genre', 'rating']
    success_url = '/music/albums'

class CoverCreateView(CreateView):
    model = Cover
    fields = ['cover', 'name']
    success_url = '/music/albums'


class GenreCreateView(CreateView):
    model = Genre
    fields = ['name',]
    success_url = '/music/albums'


class AuthorCreateView(CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'pseudonim', 'city']
    success_url = '/music/albums'


class CountryCreateView(CreateView):
    model = Genre
    fields = ['country',]
    success_url = '/music/albums'


class CityCreateView(CreateView):
    model = Genre
    fields = ['city', 'country']
    success_url = '/music/albums'