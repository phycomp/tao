from django.urls import include, path, re_path
from .views import GalleryMediaDescription, GalleryMediaDelete, GalleryPagination, GalleryDelete, GalleryEdit, GalleryAdd, GalleryDetail, Galleries	#, GalleryCommentSelfEdit, GalleryCommentEdit, GalleryCommentSelfDelete, GalleryCommentDelete, GalleryCommentSelf, GallerySearch, GalleryContextEdit, GalleryAdd, GalleryComment	#, Gallery, GenericPostAdd


urlpatterns=[
    path(r'', Galleries.as_view(), name='gallery'),
    path(r'detail/<int:gid>/', GalleryDetail.as_view(), name='gallery-detail'),
    path(r'add/', GalleryAdd.as_view(), name='gallery-add'),
    path(r'delete/', GalleryDelete.as_view(), name='gallery-delete'),
    path(r'gallery-pagination/', GalleryPagination.as_view(), name='gallery-pagination'),
    path(r'media-delete/', GalleryMediaDelete.as_view(), name='gallery-media-delete'),
    path(r'media-decription/', GalleryMediaDescription.as_view(), name='gallery-media-decription'),
    path(r'edit/', GalleryEdit.as_view(), name='gallery-edit'),
    #path(r'gallery/', Gallery.as_view(), name='gallery'),
    #path(r'add/', GalleryAdd.as_view(), name='gallery-add'),
    #path(r'context-edit/', GalleryContextEdit.as_view(), name='gallery-context-edit'),
    #path(r'search/', GallerySearch.as_view(), name='gallery-search'),
    #path(r'comment/', GalleryComment.as_view(), name='gallery-comment'),
    #path(r'comment-edit/', GalleryCommentEdit.as_view(), name='gallery-comment-edit'),
    #path(r'comment-delete/', GalleryCommentDelete.as_view(), name='gallery-comment-delete'),
    #path(r'comment-self/', GalleryCommentSelf.as_view(), name='gallery-comment-self'),
    #path(r'comment-self-edit/', GalleryCommentSelfEdit.as_view(), name='gallery-comment-self-edit'),
    #path(r'comment-self-delete/', GalleryCommentSelfDelete.as_view(), name='gallery-comment-self-delete'),
    #re_path(r'(?P<gid>\d+)/', GalleryEdit.as_view(), name='gallery-edit'),
    #re_path(r'delete/(?P<gid>\d+)/', GalleryDelete.as_view(), name='gallery-delete'),
    #path(r'generic-post-add/', GenericPostAdd.as_view(), name='generic-post-add'),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
