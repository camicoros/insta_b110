from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render

from .models import Post


def index(request):
    posts = Post.objects.all().annotate(
        likes_count=Count('likes')
    ).order_by(
        '-likes_count'
    )[:10]
    output = (
        f"<div>pk: {post.pk}| name: {post.name}| likes: {post.likes_count}</div>"
        for post in posts
    )
    return HttpResponse(output)


def lenta_of_posts(request):
    response = "Здесь все посты"
    return HttpResponse(response)


def post_detail(request, post_pk):
    response = f"Это страница поста {post_pk}"
    return HttpResponse(response)