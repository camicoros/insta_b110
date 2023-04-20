from django.urls import path

from .views import index, lenta_of_posts, post_create, post_detail


app_name = 'posts'

urlpatterns = [
    path('', index, name='index'),
    path('lenta/', lenta_of_posts, name='lenta'),
    path('<int:post_pk>/', post_detail, name='post-detail'),
    path('post-create/', post_create, name='post-create'),
]