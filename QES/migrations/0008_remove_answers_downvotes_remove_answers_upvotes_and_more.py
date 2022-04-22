# Generated by Django 4.0.4 on 2022-04-22 04:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('QES', '0007_alter_questions_upvotes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='downvotes',
        ),
        migrations.RemoveField(
            model_name='answers',
            name='upvotes',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='downvotes',
        ),
        migrations.AddField(
            model_name='answers',
            name='ans_upvotes',
            field=models.ManyToManyField(related_name='ans_upvotes', to=settings.AUTH_USER_MODEL),
        ),
    ]