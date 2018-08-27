from django.conf.urls import path
from .views import generate, get_file

urlpatterns = [
    path(r'generate/', generate, name='generate'),
    path(r'get_file/', get_file, name='get_file'),
]
