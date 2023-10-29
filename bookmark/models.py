from django.db import models
from django.urls import reverse
import uuid

class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(max_length=300)
    download = models.BooleanField(default=False)
    files = models.FileField( upload_to='bookmark/sites', max_length=100, null=True, blank=True)
    tags = models.ForeignKey('Tag', on_delete=models.SET_NULL, null=True, blank=True)
    read = models.BooleanField(default=False)
    cover = models.FileField(upload_to='bookmark/images', null=True, blank=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bookmark_detail', args=[str(self.id)])


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name