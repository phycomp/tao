from django.db.models import Model, CharField, BooleanField 
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import site, ModelAdmin

class Tag(Model):
	tag=CharField(max_length=10, unique=True)
	enabled=BooleanField(default=True)
	def __str__(self): return self.tag
	class Meta:
		verbose_name=_('Tag')
		verbose_name_plural=_('Tags')
		db_table='tag'

class TagAdmin(ModelAdmin): pass
site.register(Tag, TagAdmin)
