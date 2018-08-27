from django import template
from ..models import Medium
from PIL.Image import open as img_open
from django.http import HttpResponse
from base64 import b64encode
#from ..utils import ( cache_result, get_default_avatar_url, get_user_model, get_user,)


register = template.Library()

#@cache_result()
@register.simple_tag
def avatar(user, **kwargs):
	#user=a.user.get()
	avatar=user.user_avatar.earliest()
	return avatar.avatar.url
	#with img_open(avatar.avatar.path) as fin:
	#	return HttpResponse(content=fin.read(), content_type='image/png')
	response=HttpResponse(content_type='image/jpeg')
	im=img_open(avatar.avatar.path)
	im.save(response, 'JPEG')
	#print(dir(response))
	return b64encode(response.content)
	return response.content
	'''
	avatars=u.user_avatar.all()
	In [32]: u.user_avatar.get(id=1).avatar.name
	Out[32]: 'avatar/736853'
	if not isinstance(user, get_user_model()):
	try:
	user = get_user(user)
	alt = six.text_type(user)
	url = avatar_url(user, size)
	except get_user_model().DoesNotExist:
	url = get_default_avatar_url()
	alt = _("Default Avatar")
	else:
	alt = six.text_type(user)
	url = avatar_url(user, size)
	'''
