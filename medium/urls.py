from django.urls import path
from .views import AvatarRaw, AvatarMember, Thumbnail, Avatars, AvatarAdd, AvatarDelete

urlpatterns = [
    path(r'add/', AvatarAdd.as_view(), name='avatar-add'),
    path(r'delete/<int:aid>/', AvatarDelete.as_view(), name='avatar-delete'),
    path(r'all/', Avatars.as_view(), name='avatars'),
    path(r'member/<int:mid>/', AvatarMember.as_view(), name='avatar-member'),
    path(r'raw/<int:mid>/', AvatarRaw.as_view(), name='avatar-raw'),
    path(r'thumbnail/<int:aid>,<int:thumb_size>/', Thumbnail.as_view(), name='thumbnail'),
]
'''
{'thumb_size':80}, re_path, 
from .views import avatar_add, avatar_change, avatar_delete, render_primary

    path(r'change/', avatar_change, name='avatar_change'),
    path(r'delete/', avatar_delete, name='avatar_delete'),
    re_path(r'render_primary/(?P<user>[\w\d\@\.\-_]+)/(?P<size>[\d]+)/', render_primary, name='avatar_render_primary'),
'''
