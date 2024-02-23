from rest_framework import serializers
from datetime import datetime

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'time']

    def create(self, validated_data):
        """ Creates and returns a new user """
        new_post = Comment(
            user=validated_data.get('user'),
            post=validated_data.get('post'),
            content=validated_data.get('content'),
            time=datetime.utcnow()
        )

        new_post.save()
        return new_post

    def update(self, comment, validated_data):
        comment.content = validated_data.get('content')
        comment.save()
        return comment

    def time_format(self, comment):
        new_time = comment.time.strftime("%m/%d/%Y %I:%M:%S %p UTC")
        return new_time
