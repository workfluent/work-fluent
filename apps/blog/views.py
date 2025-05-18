from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Topic

def blog_list(request):
    # Fetch 5 specific topics by their names
    topics = Topic.objects.filter(name__in=["Tech", "Health", "Travel", "Education", "Lifestyle"])
    posts = BlogPost.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'blog_list.html', {'topics': topics, 'posts': posts})

def blogs_by_topic(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    posts = topic.posts.filter(is_published=True).order_by('-published_at')
    return render(request, 'blog.html', {'topic': topic, 'posts': posts})
