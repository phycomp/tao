from django.db.models import Model, ForeignKey, TextField, ManyToManyField, DateTimeField, CASCADE, CharField
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from medium.models import Medium
AUTH_USER_MODEL=settings.AUTH_USER_MODEL

class Post(Model):
	author=ForeignKey(AUTH_USER_MODEL, verbose_name=_('Author'), related_name='author_post', on_delete=CASCADE)
	body=TextField()	#editable=False
	media=ManyToManyField(Medium, related_name='media_post')
	timestamp=DateTimeField(verbose_name=_('timestamp'), auto_now=True)
	def __str__(self): return self.author.identifier
	class Meta:
		db_table='post'
		get_latest_by='timestamp'

class WallPost(Model):
	post=ForeignKey(Post, related_name='post_wallpost', on_delete=CASCADE)
	waller=ForeignKey(AUTH_USER_MODEL, verbose_name=_('Waller'), related_name='waller_wallpost', on_delete=CASCADE)
	def __str__(self): return self.waller.identifier
	class Meta: db_table='wall_post'

class CommentPost(Model):
	post=ForeignKey(Post, related_name='post_commentpost', on_delete=CASCADE)
	commentpost=ForeignKey('self', related_name='commentpost_commentpost', on_delete=CASCADE, null=True)
	commentor=ForeignKey(AUTH_USER_MODEL, verbose_name=_('Commentor'), related_name='commentor_commentpost', on_delete=CASCADE)
	body=TextField()
	timestamp=DateTimeField(_('timestamp'), auto_now=True)
	def __str__(self): return self.body[:10]
	class Meta: db_table='comment_post'
