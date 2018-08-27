from django.urls import include, path, re_path
from .views import PostAdd, PostEdit, PostDetail, PostCommentSelf, PostCommentSelfEdit, PostCommentSelfDelete, PostContextEdit, PostCommentEdit, PostCommentDelete, PostDelete, PostComment, WallAdd, PostMediaDelete	#PostPagination, 

urlpatterns=[
    #path(r'pagination/', PostPagination.as_view(), name='post-pagination'),
    path(r'add/', PostAdd.as_view(), name='post-add'),
    path(r'wall-add/', WallAdd.as_view(), name='wall-add'),
    path(r'edit/', PostEdit.as_view(), name='post-edit'),
    #path(r'edit/<int:pid>/', PostEdit.as_view(), name='post-edit'),
    path(r'delete/', PostDelete.as_view(), name='post-delete'),
    path(r'detail/<int:pid>/', PostDetail.as_view(), name='post-detail'),
    path(r'comment/', PostComment.as_view(), name='post-comment'),
    path(r'comment-delete/', PostCommentDelete.as_view(), name='post-comment-delete'),
    path(r'comment-edit/', PostCommentEdit.as_view(), name='post-comment-edit'),
    path(r'context-edit/', PostContextEdit.as_view(), name='post-context-edit'),
    path(r'comment-self/', PostCommentSelf.as_view(), name='post-comment-self'),
    path(r'comment-self-delete/', PostCommentSelfDelete.as_view(), name='post-comment-self-delete'),
    path(r'comment-self-edit/', PostCommentSelfEdit.as_view(), name='post-comment-self-edit'),
    path(r'media-delete/', PostMediaDelete.as_view(), name='post-media-delete'),
]
