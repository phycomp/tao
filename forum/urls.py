from django.urls import include, path, re_path
from .views import ForumPagination, ForumReplyDelete, ForumReplyEdit, ForumMediaDelete, ForumReply, ForumSelf, ForumContextEdit, ForumDetail, ForumEdit, ForumAdd, ForumDelete, Forums, ForumSelfDelete, ForumSelfEdit	#, ForumComment, 	#BlogCommentEdit, BlogCommentDelete, BlogCommentSelf, WallAdd, BlogSearch, Blogs, BlogComment, GenericPostAdd


urlpatterns=[
    path(r'', Forums.as_view(), name='forums'),
    path(r'add/', ForumAdd.as_view(), name='forum-add'),
    path(r'detail/<int:fid>/', ForumDetail.as_view(), name='forum-detail'),
    path(r'edit/', ForumEdit.as_view(), name='forum-edit'),
    path(r'delete/', ForumDelete.as_view(), name='forum-delete'),
    path(r'context-edit/', ForumContextEdit.as_view(), name='forum-context-edit'),
    path(r'media-delete/', ForumMediaDelete.as_view(), name='forum-media-delete'),
    path(r'self/', ForumSelf.as_view(), name='forum-self'),
    path(r'self-edit/', ForumSelfEdit.as_view(), name='forum-self-edit'),
    path(r'self-delete/', ForumSelfDelete.as_view(), name='forum-self-delete'),
    path(r'reply/', ForumReply.as_view(), name='forum-reply'),
    path(r'reply-edit/', ForumReplyEdit.as_view(), name='forum-reply-edit'),
    path(r'reply-delete/', ForumReplyDelete.as_view(), name='forum-reply-delete'),
    path(r'forum-pagination/', ForumPagination.as_view(), name='forum-pagination'),
    #path(r'comment/', ForumComment.as_view(), name='forum-comment'),
    #path(r'wall-add/', WallAdd.as_view(), name='wall-add'),
    #path(r'search/', BlogSearch.as_view(), name='blog-search'),
    #re_path(r'(?P<bid>\d+)/', BlogEdit.as_view(), name='blog-edit'),
    #re_path(r'delete/(?P<bid>\d+)/', BlogDelete.as_view(), name='blog-delete'),
]
