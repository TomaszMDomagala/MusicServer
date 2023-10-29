from django.db import models
from django.urls import reverse
import uuid


RATING = (
        (' ', 'None'),
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three'),
        ('4', 'Four'),
        ('5', "Five"),
    )


class Genre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Song(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    audio = models.FileField(upload_to='music/audio')
    cover = models.ForeignKey('Cover', on_delete=models.SET_NULL, null=True)
    duration = models.PositiveIntegerField()
    last_played = models.DateTimeField(null=True, blank=True)
    lyric = models.TextField(blank=True, null=True)
    genre = models.ManyToManyField(Genre)

    rating = models.CharField(
        max_length=1,
        choices=RATING,
        blank=True,
        default=' ',
    )
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('song_detail', args=[str(self.id)])


class Cover(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cover = models.FileField(upload_to='music/images')
    title = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('song_cover', args=[str(self.id)])


class Album(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    songs = models.ManyToManyField(Song)
    title = models.CharField(max_length=100)
    cover = models.ForeignKey('Cover', on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    date = models.DateField(null=True, blank=True)
    genre = models.ManyToManyField(Genre)

    rating = models.CharField(
        max_length=1,
        choices=RATING,
        blank=True,
        default=' ',
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('album_detail', args=[str(self.id)])


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    pseudonim = models.CharField(max_length=100, null=True, blank=True)
    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        if not self.pseudonim:
            return f"{self.first_name} {self.last_name}"
        else:
            return f"{self.pseudonim}"


class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country = models.CharField(max_length=40, null=True, blank=True)
      
    def __str__(self):
        return self.country


class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    city = models.CharField(max_length=40, null=True, blank=True)
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.city