from django.db import migrations

def add_initial_topics(apps, schema_editor):
    Topic = apps.get_model('blog', 'Topic')
    topics = [
        {"name": "Tech", "slug": "tech"},
        {"name": "Health", "slug": "health"},
        {"name": "Travel", "slug": "travel"},
        {"name": "Education", "slug": "education"},
        {"name": "Lifestyle", "slug": "lifestyle"},
    ]
    for topic in topics:
        Topic.objects.create(**topic)

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_add_topic_model'),
    ]

    operations = [
        migrations.RunPython(add_initial_topics),
    ]
