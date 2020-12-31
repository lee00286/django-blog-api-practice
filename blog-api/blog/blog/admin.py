from django.contrib import admin
from blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Display id, title, modify_dt
    list_display = ('id', 'title', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('title', 'content')
    # Fill slug with title
    prepopulated_fields = {'slug': ('title',)}
