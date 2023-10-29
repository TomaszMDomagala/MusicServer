from django.views.generic import CreateView, ListView, DetailView
from django.http import HttpResponse, HttpResponseRedirect
from .models import Bookmark, Tag
from .page_collector import download_page
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)


class BookmarkListView(ListView):
    model = Bookmark


class BookmarkDetailView(DetailView):
    model = Bookmark


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['name', 'description', 'url', 'download', 'read', 'tags']
    success_url = '/bookmark/bookmarks'

    def form_valid(self, form):
        # download_page(form.instance.url, 'bookmark/sites')
        return super().form_valid(form)

class TagCreateView(CreateView):
    model = Tag
    fields = ['name', ]
    success_url = '/bookmark/bookmarks'
