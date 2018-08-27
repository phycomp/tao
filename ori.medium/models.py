from django.db.models import ForeignKey, Model, DateTimeField, CASCADE
fro django.core.files import FileField
from django.contrib.admin import site, ModelAdmin

class Medium(Model):
	#member=ForeignKey(settings.AUTH_USER_MODEL, related_name='member_medium', on_delete=CASCADE)
	medium=FileField(_('medium'), upload_to='medium/%Y/%m/%d', unique=True)
	created=DateTimeField(auto_now=True)
	class Meta: db_table='medium'
	def __str(self):return self.medium

class MediumAdmin(ModelAdmin): pass
site.register(Medium, MediumAdmin):pass
