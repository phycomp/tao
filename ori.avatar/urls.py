from django.urls import path, re_path

from avatar.views import avatar_add, avatar_change, avatar_delete, render_primary

urlpatterns = [
    path(r'add/', avatar_add, name='avatar_add'),
    path(r'change/', avatar_change, name='avatar_change'),
    path(r'delete/', avatar_delete, name='avatar_delete'),
    re_path(r'render_primary/(?P<user>[\w\d\@\.\-_]+)/(?P<size>[\d]+)/', render_primary, name='avatar_render_primary'),
]
