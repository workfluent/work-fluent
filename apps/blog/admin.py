from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'is_published', 'published_at')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('is_published', 'created_at')
    search_fields = ('title',)