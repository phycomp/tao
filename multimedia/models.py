from django.db.models import Manager, Model, DateTimeField, CharField, TextField, ForeignKey, FileField, BooleanField, ManyToManyField, CASCADE
from django.core.files import File
from hashlib import sha1

class MediaManager(Manager):
	def active(self): return self.filter(active=True)
	def by_container(self, containers): return self.filter(remotestorage__profile__container__in=containers).distinct()
	def by_profile(self, profiles): return self.filter(remotestorage__profile__in=profiles).distinct()

@python_2_unicode_compatible
class Media(Model):
	"""A media file to be encoded and uploaded to a remote server."""
	owner=ForeignKey(settings.AUTH_USER_MODEL, related_name='owner_media', verbose_name=_('owner'), editable=False, on_delete=CASCADE)
	youtube=CharField(max_length=30, unique=True)
	#title=CharField(_('title'), max_length=255)
	#description=TextField(_('description'), blank=True)
	multimedia=FileField(_('multimedia'), upload_to='multimedia/%Y/%m/%d', unique=True)
	created=DateTimeField(_('created'), editable=False)
	#modified=DateTimeField(_('modified'), editable=False)
	#profiles=ManyToManyField(EncodeProfile)
	active=BooleanField(default=False, editable=False)
	objects=MediaManager()
	class Meta:
		verbose_name = _('Media')
		verbose_name_plural = _('Medium')
	def __str__(self): return self.title
	def save(self, *args, **kwargs):
		if not self.id: self.created = now()
		self.modified = now()
		super(Media, self).save(*args, **kwargs)
	def generate_content_hash(self, path, chunk_size=None):
		"""Return a SHA1 hash of the file's contents."""
		if not chunk_size: chunk_size = File.DEFAULT_CHUNK_SIZE
		hashEncryp = sha1()
		with open(path, 'rb') as f:
			while True:
				chunk = f.read(chunk_size)
				if not chunk: break
				sha1.update(chunk)
		return sha1.hexdigest()
