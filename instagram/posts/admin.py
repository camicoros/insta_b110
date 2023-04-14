from django.contrib import admin

from .models import Comment, HashTag, Post


admin.site.register(Comment)
admin.site.register(HashTag)
admin.site.register(Post)
