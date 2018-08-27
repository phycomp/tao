from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, StreamingHttpResponse
from django.views import View
from django.urls import reverse
from json import dumps
from PIL.Image import open as img_open
from .models import Medium
from django.contrib.auth import get_user_model
from os.path import join as path_join
from magic import from_file as magic_file
from io import BytesIO
User=get_user_model()

class AvatarDelete(View):
	def get(self, request, aid=None):
		HTTP_REFERER=request.META['HTTP_REFERER']
		me, avatarOBJ=request.user, Medium.objects.get(id=aid)
		me.avatar.remove(avatarOBJ)
		#avatar.primary=True
		#AvatarOBJ.save(avatar_file.name, avatar_file)
		return HttpResponseRedirect(HTTP_REFERER)
		return render(request, 'avatar-add.html')
	def post(self, request): pass

class AvatarAdd(View):
	#def get(self, request): return render(request, 'avatar-add.html')
	def post(self, request):
		me, media=request.user, request.FILES['avatar']
		mdm=me.user_medium.create(media=media, isAvatar=True)
		from base64 import b64encode
		from io import BytesIO
		buffered = BytesIO()
		image=img_open(mdm.media.path)
		image.save(buffered, format="JPEG")
		b64Str=b64encode(buffered.getvalue()).decode()
		#b64Str=str(b64Str)
		return JsonResponse(dumps({'avatarAdded':True, 'media':b64Str}), content_type='application/json', safe=False)
		return HttpResponseRedirect(reverse('avatar-add'))

def streamResponse(media, chunksize=8192):
	with open(media.media.path, 'rb') as video_file:
		byte = video_file.read(chunksize)
		while byte: yield byte
	return StreamingHttpResponse(read(), content_type='video/mp4')

def stream(full_path, mode='inline', contentType=None):
	from django.utils.encoding import escape_uri_path
	filename=full_path.split('/')[-1]
	filename=escape_uri_path(filename)
	with open(full_path, 'rb') as clip:
		response = HttpResponse(clip.read(), content_type=contentType)
		#response['Content-Disposition']='{}; filename= "{}"'.format(mode, media.filename)
		response['Content-Disposition']='%s; filename=%s' %(mode, filename)
		return response

class AvatarRaw(View):
	def get(self, request, mid=None):
		media=Medium.objects.get(id=mid)
		full_path=media.media.path
		#assert magic_file(avatar.media.path)=='image/jpeg', 'Error'
		#PDF, textPython, textPlain, textHtml, videoMP4='application/pdf', 'text/x-python', 'text/plain', 'text/html', 'video/mp4'
		#textPlain, textPython, textHtml, PDF, 
		mime_type=magic_file(full_path, mime=True)
		#print(mime_type)
		if mime_type in ['image/jpeg', 'image/png', 'image/gif']:
			response=HttpResponse(content_type=mime_type)	#'image/png')
			im=img_open(full_path)
			im.save(response, 'PNG')
			return response
		elif mime_type in ['application/pdf', 'text/x-python', 'text/plain', 'text/html', 'video/mpeg', 'video/mp4', 'audio/mpeg']:
			return stream(full_path, contentType=mime_type)
		#elif mime_type in []:
		#	return stream(full_path, contentType=mime_type)
		#	return HttpResponse(content, content_type='text/plain; charset=utf-8')
		#elif mime_type in [PDF]:
		#	return stream(full_path, contentType=mime_type)
		#	return pdfResponse(media)
		else:
			return stream(full_path, mode='attachment', contentType='application/octet-stream')
			#response['Content-Disposition']='attachment; filename= "%s"'%media.filename
			#'application/vnd.oasis.opendocument.presentation'
	
class AvatarMember(View):
	def get(self, request, mid=None):
		response=HttpResponse(content_type='image/png')
		member=User.objects.get(id=mid)
		avatar=member.user_medium.filter(isAvatar=True).last()
		im=img_open(avatar.media.path)
		im.save(response, 'PNG')
		return response

class Avatars(View):
	def get(self, request):
		me=request.user
		avatars=me.avatar.all()
		return render(request, 'avatars.html', {'avatars':avatars})
		response=HttpResponse(content_type='image/png')
		user=request.user
		avatar=user.user_avatar.earliest()
		im=img_open(avatar.media.path)
		return response

class Thumbnail(View):
	def get(self, request, aid=None, thumb_size=None):
		response=HttpResponse(content_type='image/png')
		if aid:
			avatar=Medium.objects.get(id=aid)
			im=img_open(avatar.media.path)
		else:
			avatardefault=path_join(settings.MEDIA_ROOT, Avatar.avatar.field.default)
			im=img_open(avatardefault)
		thumb_size=int(thumb_size)
		im.thumbnail((thumb_size, thumb_size))
		im.save(response, 'PNG')
		return response
'''
def create_thumbnail(image, thumb_size=None):
	w, h = image.size
	if w != thumb_size or h != thumb_size:
		if w > h:
			diff = int((w - h) / 2)
			image = image.crop((diff, 0, w - diff, h))
		else:
			diff = int((h - w) / 2)
			image = image.crop((0, diff, w, h - diff))
		if image.mode not in ('RGB', 'RGBA'): image = image.convert('RGB')
		image = image.resize((thumb_size, thumb_size))
		thumb = BytesIO()
		image.save(thumb, 'PNG')	#, settings.AVATAR_THUMB_FORMAT, quality=quality)
		return thumb
		#thumb_file = ContentFile(thumb.getvalue())

		#thumb=create_thumbnail(im, thumb_size=thumb_size)
		#im.thumbnail((80, 80))
		#im.save(response, 'PNG')
		return response

def pdfResponse(media):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition']='attachment; filename="%s"'%media.media.name
	with open(media.media.path, 'rb') as pdfHndlr:
		pdfContents=pdfHndlr.read()
	return HttpResponse(pdfContents, mimetype='application/pdf')
	return response

'''
