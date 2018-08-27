from django.db.models import CharField, ForeignKey, FileField, Model, ManyToManyField, DateTimeField, CASCADE, BooleanField
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.utils.datetime_safe import date
from os.path import splitext
from magic import from_file as magic_file

def uploadMedium(instance, filename):
	#base, ext=splitext(filename)
	#today=date.today().toordinal()
	#return 'medium/%s-%s%s'%(today, base, ext)
	return 'medium/%s'%filename
	#return '%s'%filename

class MediumManager(BaseUserManager):
	def upload_media(self, filename=None, **kwargs):
		with open(filename, 'rb') as fin:
			for chunk in fin.chunks():
				fin.write(chunk)
		pass

class Medium(Model):
	user=ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_medium')
	media=FileField(upload_to=uploadMedium, default='medium/default.png')	#'medium/%s'%filename
	description=CharField(max_length=50, null=True)
	#user=ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_medium')
	#avatar=ImageField(upload_to=uploadAvatar, default='avatar/default.png')
	isAvatar=BooleanField(default=False)
	timestamp=DateTimeField(verbose_name=_('timestamp'),auto_now=True)
	def __str__(self): return self.media.name
	@property
	def filename(self): return self.media.name.split('/')[-1]
	@property
	def contentType(self):
		return magic_file(self.media.path, mime=True)
		return True if mime_type=='text/plain' else False
	'''
	objects=MediumManager()
	@property
	def latest(self):return self.user.avatar.latest()
	'''
	class Meta:
		db_table='medium'
		get_latest_by='date_uploaded'
