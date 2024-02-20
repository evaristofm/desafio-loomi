# Generated by Django 5.0.2 on 2024-02-20 19:03

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_likes_count_like_post_likes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='comments_count',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('body', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(blank=True, to='post.comment'),
        ),
        migrations.CreateModel(
            name='PostAttachment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='post_attachments')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_attachments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='attachments',
            field=models.ManyToManyField(blank=True, to='post.postattachment'),
        ),
    ]
