from django.contrib.admin import ModelAdmin, site
from .models import Member

class MemberAdmin(ModelAdmin):
    list_display=('identifier', 'last_name', 'first_name', 'address', 'email',)
    list_editable=('email',)
    #list_filter=( 'address__city', 'address__city__state', 'address__city__county', 'company',)
    ordering=('last_name', 'first_name')
    #readonly_fields=('phone',)
    search_fields=('last_name', 'first_name', 'address__name', 'email')

site.register(Member, MemberAdmin)
