from django.conf import settings

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic.base import TemplateView
from .views import HOME, ContactView, HomePagination, AddCreditCard
#from notifications import urls as notifurls
from haystack.generic_views import SearchView

urlpatterns = [
    #path(r'tts/', include('tts.urls')),
    #path(r'qr/', include('qrauth.urls')),
    path(r'search/', include('haystack.urls')),
    path(r'access/', TemplateView.as_view(template_name='access.html'), name='access'),
    #path(r'search/', SearchView.as_view(template_name='search/search.html'), name='search'),
    path(r'simplesearch/', TemplateView.as_view(template_name='simplesearch.html'), name='simplesearch'),
    path(r'credit/', TemplateView.as_view(template_name='creditcard.html'), name='credit'),
    path(r'add-credit-card/', AddCreditCard.as_view(), name='add-credit-card'),
    #path('notifications/', include(notifurls, namespace='notifications')),
    path(r'', TemplateView.as_view(template_name='index.html'), name='index'),
    path('admin/', admin.site.urls),
    path(r'home/', HOME.as_view(), name='home'),
    path(r'home-pagination/', HomePagination.as_view(), name='home-pagination'),
    path(r'contact/', ContactView.as_view(), name='contact'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('currency/', TemplateView.as_view(template_name='currency.html'), name='currency'),
    #re_path('blog/', include('pinax.blog.urls', namespace='pinax_blog')),
    #re_path(r'^account/', include('account.urls')),
    path(r'member/', include('member.urls')),
    path(r'sutra/', include('sutra.urls')),
    path(r'blog/', include('blog.urls')),
    path(r'gallery/', include('gallery.urls')),
    path(r'ge2ge/', include('ge2ge.urls')),
    path(r'forum/', include('forum.urls')),
    path(r'post/', include('post.urls')),
    path(r'tag/', include('tag.urls')),
    path(r'tug/', include('tug.urls')),
    path(r'friend/', include('friend.urls')),
    path(r'medium/', include('medium.urls')),
    path('lsr/', TemplateView.as_view(template_name='login-signup-reset.html'), name='lsr'),
    path('leaflet/', TemplateView.as_view(template_name='leaflet.html'), name='leaflet'),
    path('hanzi/', TemplateView.as_view(template_name='hanzi.html'), name='hanzi'),
    path('sidebar/', TemplateView.as_view(template_name='sidebar.html'), name='sidebar'),
    path('demo/', TemplateView.as_view(template_name='demo.html'), name='demo'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView

from .views import VoteView

urlpatterns = [
    path('about/', login_required(TemplateView.as_view(template_name="secret.html"))),
    path('vote/', permission_required('polls.can_vote')(VoteView.as_view())),
]
'''
