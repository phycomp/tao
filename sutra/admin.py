from django.contrib.admin import site, ModelAdmin

from .models import Sutra, CommentSutra

class SutraAdmin(ModelAdmin):
	model=Sutra
site.register(Sutra, SutraAdmin)

class CommentSutraAdmin(ModelAdmin):
	model=CommentSutra
site.register(CommentSutra, CommentSutraAdmin)

#class SutraAdmin(ModelAdmin): pass
#site.register(Sutra, SutraAdmin)
