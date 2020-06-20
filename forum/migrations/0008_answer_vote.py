# Generated by Django 2.2 on 2020-04-13 16:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0007_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='vote',
            field=models.ManyToManyField(blank=True, related_name='votes', to=settings.AUTH_USER_MODEL),
        ),
    ]