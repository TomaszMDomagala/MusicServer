from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, TagCreateView
import uuid

urlpatterns = [
    path('bookmarks', BookmarkListView.as_view(), name="bookmark_list"),
    path('bookmarks/<uuid:pk>', BookmarkDetailView.as_view(), name="bookmark_detail"),
    path('bookmarks/create', BookmarkCreateView.as_view(), name="create_bookmark"),
    path('tag/create', TagCreateView.as_view(), name="create_tag"),
]