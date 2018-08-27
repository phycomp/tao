from django.contrib.admin import site, ModelAdmin
from .models import Forum

class ForumAdmin(ModelAdmin):
	model=Forum
site.register(Forum, ForumAdmin)
