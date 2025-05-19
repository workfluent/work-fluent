from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0002_inquiry_budget_inquiry_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='company_website',
            field=models.URLField(max_length=255, blank=True, null=True),
        ),
    ]
