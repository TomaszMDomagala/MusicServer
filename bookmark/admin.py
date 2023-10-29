from django.contrib import admin
from .models import Tag, Bookmark

admin.site.register(Bookmark)
admin.site.register(Tag)
