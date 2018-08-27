from django.urls import include, path, re_path
from .views import SutraCommentEdit, SutraCommentDelete, SutraCommentSelfEdit, SutraCommentSelfDelete, SutraCommentSelf, SutraComment, Sutras, SutraDetail, SutraBook, SutraBookChapter	#SutraAdd, SutraEdit, , SutraSection


urlpatterns = [
    path(r'', Sutras.as_view(), name='sutras'),
    #re_path(r'^$', Sutras.as_view(), name='sutras'),
    path(r'detail/<int:sid>/', SutraDetail.as_view(), name='sutra-detail'),
    #path(r'edit/<int:sid>/', SutraEdit.as_view(), name='sutra-edit'),
    #path(r'add/', SutraAdd.as_view(), name='sutra-add'),
    path(r'book/<int:bid>/', SutraBook.as_view(), name='sutra-book'),
    path(r'comment/', SutraComment.as_view(), name='sutra-comment'),
    path(r'comment-delete/', SutraCommentDelete.as_view(), name='sutra-comment-delete'),
    path(r'comment-edit/', SutraCommentEdit.as_view(), name='sutra-comment-edit'),
    path(r'comment-self/', SutraCommentSelf.as_view(), name='sutra-comment-self'),
    path(r'comment-self-delete/', SutraCommentSelfDelete.as_view(), name='sutra-comment-self-delete'),
    path(r'comment-self-edit/', SutraCommentSelfEdit.as_view(), name='sutra-comment-self-edit'),
    path(r'book/chapter/<int:bid>,<int:cid>/', SutraBookChapter.as_view(), name='sutra-book-chapter'),
    #re_path(r'book/chapter/(?P<bid>\d+),(?P<cid>\d+)/', SutraBookChapter.as_view(), name='sutra-book-chapter'),
    #re_path(r'section/(?P<sid>\d+)/$', SutraSection.as_view(), name='sutra-section'),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
