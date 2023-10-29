from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from .views import (
    SongCreateView, 
    SongListView, 
    AlbumListView, 
    AlbumDetailView, 
    PlaySong,
    AuthorCreateView,
    GenreCreateView,
    CityCreateView,
    CountryCreateView,
    CoverCreateView
    )
import uuid

urlpatterns = [
    path('songs', SongListView.as_view(), name="song_list"),
    path('albums', AlbumListView.as_view(), name="album_list"),
    path('albums/<uuid:pk>', AlbumDetailView.as_view(), name="album_detail"),
    path('play/<uuid:pk>', PlaySong.as_view(), name="song_detail"),
    path('create/song', SongCreateView.as_view(), name="create_song"),
    path('create/album', AlbumDetailView.as_view(), name="create_album"),
    path('create/author', AuthorCreateView.as_view(), name="create_author"),
    path('create/genre', GenreCreateView.as_view(), name="create_genre"),
    path('create/city', CityCreateView.as_view(), name="create_city"),
    path('create/country', CountryCreateView.as_view(), name="create_country"),
    path('create/cover', CoverCreateView.as_view(), name="create_cover"),
]