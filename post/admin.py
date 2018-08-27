from django.contrib.admin import site, ModelAdmin
from .models import Post, CommentPost, WallPost

class PostAdmin(ModelAdmin):
	model=Post
site.register(Post, PostAdmin)

class WallPostAdmin(ModelAdmin):
	model=WallPost
site.register(WallPost, WallPostAdmin)

class CommentPostAdmin(ModelAdmin):
	model=CommentPost
site.register(CommentPost, CommentPostAdmin)

