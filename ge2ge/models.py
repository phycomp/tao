from django.db.models import Model, ManyToManyField, ForeignKey, CASCADE, CharField, BooleanField, DateTimeField#, DateField, TimeField
from django.conf import settings
from gallery.models import Gallery
#from medium.models import Medium
AUTH_USER_MODEL=settings.AUTH_USER_MODEL

class GoodsExchange(Model):
	#launcher=ForeignKey(AUTH_USER_MODEL, related_name='launcher_goodsexchange', on_delete=CASCADE)
	gallery=ForeignKey(Gallery, related_name='gallery_goodsexchange', on_delete=CASCADE)
	ge2ge=ForeignKey('self', related_name='goodsexchange_goodsexchange', null=True, on_delete=CASCADE)
	coordinate=CharField(max_length=30, null=True)
	datetime=DateTimeField(null=True)
	isDealt=BooleanField(default=False)
	timestamp=DateTimeField(auto_now=True)
	class Meta:
		db_table='goodsexchange'
