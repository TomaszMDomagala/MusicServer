from django.contrib import admin
from .models import Album, Song, Genre, Author, Country, City, Cover

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Cover)