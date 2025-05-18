from django.contrib import admin
from .models import BlogPost, Topic

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'topic', 'created_at', 'is_published', 'published_at')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('is_published', 'created_at', 'topic')
    search_fields = ('title', 'topic__name')