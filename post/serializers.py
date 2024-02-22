from rest_framework import serializers

from .models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'body', 'likes_count', 'image', 'user', 'time')

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

