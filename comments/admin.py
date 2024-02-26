from django.contrib import admin

from comments.models import Like, Comment


admin.site.register(Comment)
admin.site.register(Like)


