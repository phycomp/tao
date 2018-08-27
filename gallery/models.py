from django.db.models import Model, ForeignKey, ManyToManyField, CASCADE, DateTimeField
from django.conf import settings
from blog.models import Title
from medium.models import Medium
AUTH_USER_MODEL=settings.AUTH_USER_MODEL

class Gallery(Model):
	galler=ForeignKey(AUTH_USER_MODEL, related_name='galler_gallery', on_delete=CASCADE)
	title=ForeignKey(Title, related_name='title_gallery', on_delete=CASCADE, null=True)
	picture=ManyToManyField(Medium, related_name='picture_gallery')
	#gallery=CharField(verbose_name=_('gallery'), max_length=10, null=False)
	timestamp=DateTimeField(auto_now=True)
	def __str__(self):return self.title.title
	class Meta:
		db_table='gallery'
		get_latest_by='timestamp'
