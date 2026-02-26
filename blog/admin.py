from django.contrib import admin

from .models import Comment, Like, Post, Tag
from django.contrib.auth.models import User

# Register models for admin interface

admin.site.register(User)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin interface for managing blog posts."""

    list_display = ('title', 'author', 'game_type', 'published', 'created_at')
    list_filter = ('game_type', 'published', 'created_at')
    search_fields = ('title', 'content', 'author__username')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Admin interface for managing preset tags."""

    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin interface for moderating comments."""

    list_display = ('post', 'author', 'active', 'created_at')
    list_filter = ('active', 'created_at')
    search_fields = ('post__title', 'author__username', 'body')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    """Admin interface for viewing post likes."""

    list_display = ('post', 'user', 'created_at')
    list_filter = ('created_at',)
