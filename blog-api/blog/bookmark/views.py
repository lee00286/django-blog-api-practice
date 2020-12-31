# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

# Show record list of Bookmark table
class BookmarkLV(ListView):
    model = Bookmark

# Show detail of records in Bookmark table
class BookmarkDV(DetailView):
    model = Bookmark
