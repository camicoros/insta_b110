from django.urls import path, re_path

from .views import about, about_detail, my_date

urlpatterns = [
    path('about/', about),
    path('about/<int:user_id>/', about_detail),
    re_path(r'^my-date/(?P<selected_date>\d{4}-\d{2}-\d{2})/$', my_date)
]