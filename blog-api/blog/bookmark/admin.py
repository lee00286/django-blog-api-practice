from django.contrib import admin
from bookmark.models import Bookmark

# Display id, title, url
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')
