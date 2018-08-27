from django.db.models import ForeignKey, Model, CASCADE, DateTimeField, CharField, BooleanField, TextField
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from post.models import Post
from blog.models import Title

class Forum(Model):
	title=ForeignKey(Title, related_name='title_forum', on_delete=CASCADE, null=True)
	post=ForeignKey(Post, related_name='post_forum', on_delete=CASCADE)
	selv=ForeignKey('self', related_name='selv_forum', on_delete=CASCADE, null=True)
	closed=BooleanField(default=False)
	timestamp=DateTimeField(_('timestamp'), auto_now=True)
	def __str__(self):
		return self.title.title if self.title.title else 'None'
	@property
	def forumerID(self):return self.post.author_id
	class Meta:
		db_table='forum'
		ordering=('-timestamp',)

'''
class CommentForum(Model):
	forum=ForeignKey(Forum, related_name='forum_commentforum', on_delete=CASCADE)
	commentforum=ForeignKey('self', related_name='commentforum_commentforum', on_delete=CASCADE, null=True)
	commentor=ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Commentor'), related_name='commentor_commentforum', on_delete=CASCADE)
	title=CharField(_('Title'), max_length=10, null=True)
	body=TextField()
	timestamp=DateTimeField(_('timestamp'), auto_now=True)
	def __str__(self): return self.body[:10]
	class Meta: db_table='comment_forum'
'''
