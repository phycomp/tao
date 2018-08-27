from django.urls import include, path, re_path
from .views import Tags, TagAdd, TagDetail

urlpatterns = [
    path(r'', Tags.as_view(), name='tags'),
    path(r'detail/<int:tid>/', TagDetail.as_view(), name='tag-detail'),
    path(r'add/', TagAdd.as_view(), name='tag-add'),
]
