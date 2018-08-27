#-*- coding:utf-8 -*-
from django.db.models import Model, EmailField, CharField, DateField, TextField
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class Contact(Model):
	email=EmailField(verbose_name=_('email address'), max_length=80)
	subject=CharField(verbose_name=_('subject'), max_length=20)
	body=TextField()
	def __str__(self): return ' '.join([self.email, self.subject])
	class Meta: db_table='contact'

'''
class Location(Model):
	location=CharField(max_length=20, unique=True)
	timestamp=DateField(auto_now=True)
	class Meta: db_table='location'

class Temple(Model):
	temple=CharField(max_length=5, unique=True)
	location=ForeignKey(Location, related_name='location_temple', on_delete=CASCADE)
	address=ForeignKey('Address', related_name='address_temple', on_delete=CASCADE)
	timestamp=DateField(auto_now=True)
	class Meta: db_table='temple'
	
class ZhuXien(Model):
	zhuxien=CharField(max_length=4, verbose_name='zhuxien')
	timestamp=DateField(auto_now=True)
	class Meta: db_table='zhuxien'
	
class TienZhi(Model):
	tienzhi=CharField(max_length=4, verbose_name='tienzhi')
	timestamp=DateField(auto_now=True)
	class Meta: db_table='tienzhi'

class TaoChing(Model):
	user=ForeignKey(settings.AUTH_USER_MODEL, related_name='user_taoching', on_delete=CASCADE)
	tienzhi=ManyToManyField(TienZhi, related_name='tienzhi_taoching')	#, on_delete=CASCADE)
	description=TextField(null=True)
	timestamp=DateField(auto_now=True)
	class Meta: db_table='taoching'
'''
