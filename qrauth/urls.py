from django.urls import include, path, re_path
from django.views.generic.base import TemplateView

urlpatterns = [
    re_path(r'^pic/(?P<auth_code>[a-zA-Z\d]{50})/$', 'qr_code_picture', name='auth_qr_code'),
    re_path(r'^(?P<auth_code_hash>[a-f\d]{40})/$', 'login_view', name='qr_code_login'),
    path( r'invalid_code/', TemplateView.as_view( template_name='qrauth/invalid_code.html'), name='invalid_auth_code'),
    re_path( r'^$', 'qr_code_page', name='qr_code_page'),
]
#'qrauth.views',
