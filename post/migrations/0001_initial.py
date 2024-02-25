# Generated by Django 5.0.2 on 2024-02-25 19:54

import django.db.models.deletion
import post.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=post.models.upload_image_formater)),
                ('likes_count', models.IntegerField(default=0)),
                ('comments_count', models.IntegerField(default=0)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('comments', models.ManyToManyField(blank=True, to='comments.comment')),
                ('likes', models.ManyToManyField(blank=True, to='comments.like')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
