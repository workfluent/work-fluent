from django.urls import path
from .views import blog_list, blogs_by_topic

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('topic/<slug:slug>/', blogs_by_topic, name='blogs_by_topic'),
]
