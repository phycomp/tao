from django.contrib.admin import ModelAdmin, site
from .models import Medium

class MediumAdmin(ModelAdmin):
    #list_display=('avatar', 'date_uploaded')
    #list_editable=('avatar',)
    #list_filter=( 'address__city', 'address__city__state', 'address__city__county', 'company',)
    ordering=('timestamp', )
    #readonly_fields=('phone',)
    #search_fields=('last_name', 'first_name', 'address__name', 'email')

site.register(Medium, MediumAdmin)
