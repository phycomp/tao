from django.contrib.admin import site, ModelAdmin
from .models import Blog	#, GenericPost, GenericComment

class BlogAdmin(ModelAdmin):
	model=Blog
site.register(Blog, BlogAdmin)

'''
class GenericPostAdmin(ModelAdmin):
	model=GenericPost
site.register(GenericPost, GenericPostAdmin)

class GenericCommentAdmin(ModelAdmin):
	model=GenericComment
site.register(GenericComment, GenericCommentAdmin)
'''
