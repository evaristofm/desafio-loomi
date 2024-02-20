from rest_framework import serializers

from .models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'body', 'likes_count', 'image', 'created_by', 'created_at')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'created_by', 'created_at')
