from django.test import TestCase
from django.urls import reverse
from .models import Topic, BlogPost

class TopicModelTest(TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(name="Tech", slug="tech")

    def test_topic_str(self):
        self.assertEqual(str(self.topic), "Tech")

class BlogPostModelTest(TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(name="Tech", slug="tech")
        self.blog_post = BlogPost.objects.create(
            title="Test Blog",
            slug="test-blog",
            article="This is a test blog.",
            topic=self.topic,
            is_published=True,
        )

    def test_blog_post_str(self):
        self.assertEqual(str(self.blog_post), "Test Blog")

class BlogViewsTest(TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(name="Tech", slug="tech")
        self.blog_post = BlogPost.objects.create(
            title="Test Blog",
            slug="test-blog",
            article="This is a test blog.",
            topic=self.topic,
            is_published=True,
        )

    def test_blog_list_view(self):
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tech")

    def test_blogs_by_topic_view(self):
        response = self.client.get(reverse('blogs_by_topic', args=['tech']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Blog")
