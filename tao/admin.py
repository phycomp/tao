from django.contrib.admin import ModelAdmin, site
from .models import Contact

class ContactAdmin(ModelAdmin):
    ordering=('email', 'subject')
    #list_display=('identifier', 'last_name', 'first_name', 'address', 'email',)
    #list_editable=('email',)
    #list_filter=( 'address__city', 'address__city__state', 'address__city__county', 'company',)
    #readonly_fields=('phone',)
    #search_fields=('last_name', 'first_name', 'address__name', 'email')

site.register(Contact, ContactAdmin)
