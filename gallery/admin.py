from django.contrib.admin import ModelAdmin, site
from .models import Gallery

class GalleryAdmin(ModelAdmin):
    ordering=('timestamp', )
site.register(Gallery, GalleryAdmin)
