from django.urls import path, re_path

from .views import index, about, contact, blog

urlpatterns = [
    path('', index),
    path('about/', about),
    path('contact/', contact),
    path('blog/', blog),
]