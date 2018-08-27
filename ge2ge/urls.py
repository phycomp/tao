from django.urls import include, path, re_path
from .views import GoodsExchangeApprove, GoodsExchangeDetail, GoodsExchangeStatus, GoodsExchangeMediaDelete, GoodsExchangeMediaDescription, GoodsExchangeApply, GoodsExchangeEdit, GoodsExchangeDelete, GoodsExchangePagination, GoodsExchangeInvoke, GoodsExchanges#GoodsExchangeAdd, Galleries	, GoodsExchangeCommentSelfEdit, GoodsExchangeCommentEdit, GoodsExchangeCommentSelfDelete, GoodsExchangeCommentDelete, GoodsExchangeCommentSelf, GoodsExchangeSearch, GoodsExchangeContextEdit, GoodsExchangeComment, GoodsExchange, GenericPostAdd


urlpatterns=[
    path(r'', GoodsExchanges.as_view(), name='goods-exchange'),
    path(r'invoke/', GoodsExchangeInvoke.as_view(), name='ge-invoke'),
    path(r'apply/<int:gid>/', GoodsExchangeApply.as_view(), name='ge-apply'),
    path(r'status/', GoodsExchangeStatus.as_view(), name='ge-status'),
    path(r'ge-pagination/', GoodsExchangePagination.as_view(), name='ge-pagination'),
    path(r'delete/', GoodsExchangeDelete.as_view(), name='ge-delete'),
    path(r'edit/<int:gid>/', GoodsExchangeEdit.as_view(), name='ge-edit'),
    path(r'media-decription/', GoodsExchangeMediaDescription.as_view(), name='ge-media-decription'),
    path(r'media-delete/', GoodsExchangeMediaDelete.as_view(), name='ge-media-delete'),
    path(r'detail/<int:gid>/', GoodsExchangeDetail.as_view(), name='ge-detail'),
    path(r'approve/', GoodsExchangeApprove.as_view(), name='ge-approve'),
    #path(r'ge/', GoodsExchange.as_view(), name='ge'),
    #path(r'context-edit/', GoodsExchangeContextEdit.as_view(), name='ge-context-edit'),
    #path(r'search/', GoodsExchangeSearch.as_view(), name='ge-search'),
    #path(r'comment/', GoodsExchangeComment.as_view(), name='ge-comment'),
    #path(r'comment-edit/', GoodsExchangeCommentEdit.as_view(), name='ge-comment-edit'),
    #path(r'comment-delete/', GoodsExchangeCommentDelete.as_view(), name='ge-comment-delete'),
    #path(r'comment-self/', GoodsExchangeCommentSelf.as_view(), name='ge-comment-self'),
    #path(r'comment-self-edit/', GoodsExchangeCommentSelfEdit.as_view(), name='ge-comment-self-edit'),
    #path(r'comment-self-delete/', GoodsExchangeCommentSelfDelete.as_view(), name='ge-comment-self-delete'),
    #re_path(r'(?P<gid>\d+)/', GoodsExchangeEdit.as_view(), name='ge-edit'),
    #re_path(r'delete/(?P<gid>\d+)/', GoodsExchangeDelete.as_view(), name='ge-delete'),
    #path(r'generic-post-add/', GenericPostAdd.as_view(), name='generic-post-add'),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
