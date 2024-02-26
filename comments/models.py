from django.db import models

from account.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('content',)

    def __str__(self):
        return self.content


class Like(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="user_like")
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)





