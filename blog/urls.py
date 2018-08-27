from django.urls import include, path, re_path
from .views import BlogMediaDelete, BlogPagination, BlogCommentSelfEdit, BlogCommentEdit, BlogCommentSelfDelete, BlogCommentDelete, BlogCommentSelf, BlogSearch, Blogs, BlogDetail, BlogEdit, BlogContextEdit, BlogDelete, BlogAdd, BlogComment	#, GenericPostAdd


urlpatterns=[
    path(r'', Blogs.as_view(), name='blogs'),
    path(r'blog-pagination/', BlogPagination.as_view(), name='blog-pagination'),
    path(r'add/', BlogAdd.as_view(), name='blog-add'),
    path(r'delete/', BlogDelete.as_view(), name='blog-delete'),
    path(r'edit/', BlogEdit.as_view(), name='blog-edit'),
    #path(r'edit/<int:bid>/', BlogEdit.as_view(), name='blog-edit'),
    path(r'context-edit/', BlogContextEdit.as_view(), name='blog-context-edit'),
    path(r'detail/<int:bid>/', BlogDetail.as_view(), name='blog-detail'),
    path(r'search/', BlogSearch.as_view(), name='blog-search'),
    path(r'comment/', BlogComment.as_view(), name='blog-comment'),
    path(r'comment-edit/', BlogCommentEdit.as_view(), name='blog-comment-edit'),
    path(r'comment-delete/', BlogCommentDelete.as_view(), name='blog-comment-delete'),
    path(r'comment-self/', BlogCommentSelf.as_view(), name='blog-comment-self'),
    path(r'comment-self-edit/', BlogCommentSelfEdit.as_view(), name='blog-comment-self-edit'),
    path(r'comment-self-delete/', BlogCommentSelfDelete.as_view(), name='blog-comment-self-delete'),
    path(r'media-delete/', BlogMediaDelete.as_view(), name='blog-media-delete'),
    #re_path(r'(?P<bid>\d+)/', BlogEdit.as_view(), name='blog-edit'),
    #re_path(r'delete/(?P<bid>\d+)/', BlogDelete.as_view(), name='blog-delete'),
    #path(r'generic-post-add/', GenericPostAdd.as_view(), name='generic-post-add'),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
