import os
import uuid
from django.db import models

from account.models import User
from comments.models import Like, Comment


def upload_image_formater(instance, filename):
    return f'{str(uuid.uuid4())}-{filename}'


class Post(models.Model):
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_image_formater, blank=True, null=True)
    likes_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment, blank=True)
    likes = models.ManyToManyField(Like, blank=True)

    def has_image(self):
        return self.image is not None and self.image != ''

    def remove_image(self):
        if self.has_image():
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)

    def delete(self):
        self.remove_image()
        super().delete()

    def __str__(self):
        return self.body
