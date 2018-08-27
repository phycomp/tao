from django import template
register = template.Library()
from sutra.models import CommentSutra
from blog.models import CommentBlog

@register.filter(is_safe=True)
def isImage(ins):
	return True if ins.contentType in ['image/jpeg', 'image/png', 'image/gif'] else False
	return True if ins.contentType in ['text/x-python', 'text/plain'] else False

@register.filter
def commenttugself(ins, **kwargs):
	return ins.commentsutra_commentsutra.exclude(commentsutra=None)

@register.filter
def commentsutraself(ins, **kwargs):
	return ins.commentsutra_commentsutra.exclude(commentsutra_id__isnull=False)

@register.filter
def commentblogself(ins, **kwargs):
	return ins.commentblog_commentblog.exclude(commentblog=None)
	return ins.commentblog_commentblog.exclude(commentblog_id__isnull=True)
	blog=ins.blog
	return blog.blog_commentblog.filter(commentblog=ins)

@register.filter
def commentpostself(ins, **kwargs):
	return ins.commentpost_commentpost.exclude(commentpost=None)
'''
@register.filter
def forumself(ins, **kwargs):
	#print(len(ins.forum_forum.exclude(title=True)))
	return ins.forum_forum.all()	#exclude(title=True)

	post=ins.post
	return post.post_commentpost.filter(commentpost=ins)
	sutra=ins.sutra
	return sutra.sutra_commentsutra.exclude(commentsutra=None)
	return sutra.sutra_commentsutra.filter(commentsutra=ins)
	blog=ins.blog
	return CommentSutra.objects.filter(sutra=sutra, commentsutra=ins)
	return CommentBlog.objects.filter(blog=blog, commentblog=ins)
	CommentSutra.objects.filter(sutra=sutra).filter(commentsutra=cmt).exclude(commentsutra=None)
	return CommentSutra.objects.filter(sutra=sutra, commentsutra=ins).exclude(commentsutra=None)
	return ins.sutra_commentsutra.filter(commentsutra__isnull=False)
from ..models import Medium
from PIL.Image import open as img_open
from django.http import HttpResponse
from base64 import b64encode
#from ..utils import ( cache_result, get_default_avatar_url, get_user_model, get_user,)


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

'''
@register.filter(is_safe=True)
def grant_permission(ins, user):
	if hasattr(ins, 'author'): return True if ins.author==user else False
	elif hasattr(ins, 'post'): return True if ins.post.author==user else False
	elif hasattr(ins, 'initiator'): return True if ins.initiator==user else False
	elif hasattr(ins, 'gallery'): return True if ins.gallery.galler==user else False
	elif hasattr(ins, 'blog'): return True if ins.blog.post.author==user else False
	else:
		print(ins==user)
		return True if ins==user else False
	elif hasattr(ins, 'launcher'): return True if ins.launcher.get()==user else False
	elif hasattr(ins, 'commentblog'):
		commentblog=ins.commentblog
		if hasattr(commentblog, 'post'):
			post=commentblog.post
			return True if post.author==user else False
'''
