from django.db.models import Model, ForeignKey, CharField, TextField, DateTimeField, CASCADE, ManyToManyField	#, PositiveSmallIntegerField
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
#from django.contrib.contenttypes.fields import ContentType, GenericForeignKey, GenericRelation
from tag.models import Tag
from post.models import Post
AUTH_USER_MODEL=settings.AUTH_USER_MODEL

class Title(Model):
	title=CharField(_('Title'), max_length=20)
	timestamp=DateTimeField(_('timestamp'), auto_now=True)
	class Meta: db_table='title'

class Blog(Model):
	title=ForeignKey(Title, related_name='title_blog', on_delete=CASCADE)
	post=ForeignKey(Post, related_name='post_blog', on_delete=CASCADE)
	tag=ManyToManyField(Tag, related_name='tag_blog')
	timestamp=DateTimeField(_('timestamp'), auto_now=True)
	def __str__(self): return self.post.author.identifier
	@property
	def bloggerID(self): return self.post.author_id
	class Meta:
		db_table='blog'
		get_latest_by='timestamp'

class CommentBlog(Model):
	blog=ForeignKey(Blog, related_name='blog_commentblog', on_delete=CASCADE)
	commentblog=ForeignKey('self', related_name='commentblog_commentblog', on_delete=CASCADE, null=True)
	commentor=ForeignKey(AUTH_USER_MODEL, verbose_name=_('Commentor'), related_name='commentor_commentblog', on_delete=CASCADE)
	body=TextField()
	timestamp=DateTimeField(_('timestamp'), auto_now=True)
	def __str__(self): return self.body[:10]
	class Meta:
		db_table='comment_blog'
		get_latest_by='timestamp'

'''
	@property
	def commentorID(self): return self.commentor_id
class GenericPost(Model):
	content_type=ForeignKey(ContentType, related_name='contenttype_genericpost', on_delete=CASCADE)
	object_id=PositiveSmallIntegerField()
	content_object=GenericForeignKey('content_type', 'object_id')
	timestamp=DateTimeField(auto_now=True)
	def __str__(self):return ' '.join([self.content_object.__str__(), self.content_type.app_label, self.content_type.name])
	class Meta:db_table='generic_post'

class GenericComment(Model):
	general_post=GenericRelation(GenericPost)
	content_type=ForeignKey(ContentType, related_name='contenttype_genericcomment', on_delete=CASCADE)
	object_id=PositiveSmallIntegerField()
	content_object=GenericForeignKey('content_type', 'object_id')
	timestamp=DateTimeField(auto_now=True)
	def __str__(self):return ' '.join([self.content_object.__str__(), self.content_type.app_label, self.content_type.name])
	class Meta:db_table='generic_comment'
gp.content_type.contenttype_genericpost.all()
ContentType.objects.get_for_model(Post)
Out[52]: <ContentType: post>
ggpp=GenericPost.objects.get(id=1)
ContentType.objects.get(contenttype_genericpost=ggpp)
postCT=ContentType.objects.get(contenttype_genericpost=ggpp)
gp=GenericPost.objects.create(content_type=postCT, object_id=3)
<GenericPost: post>
gp.content_object=p
In [86]: gp.save()

In [87]: post=u.author_post.create(body='kxjldjlkj\nkdjkfjldj\nkdjfldjldjfld')
Out[87]: <Post: P121868381>

In [88]: ContentType.objects.get_for_model(Post)
Out[88]: <ContentType: post>

In [89]: pCT=ContentType.objects.get_for_model(Post)
In [90]: pCT.contenttype_genericpost.create(content_object=post)
Out[90]: <GenericPost: post>

p.media.exists()
'''
