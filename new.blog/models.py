from django.db.models import Model, ForeignKey, CharField, TextField, DateTimeField, CASCADE, ManyToManyField	#, PositiveSmallIntegerField
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
#from django.contrib.contenttypes.fields import ContentType, GenericForeignKey, GenericRelation
from tag.models import Tag
from post.models import Post

class BlogBase(Post):
	title=CharField(verbose_name=_('Title'), max_length=10)
	#timestamp=DateTimeField(verbose_name=_('timestamp'), auto_now=True)
	class Meta:
		db_table='title'
