from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views import View
from django.template import loader
from django.template.response import TemplateResponse

#from magic import from_file as magic_file
from .models import Gallery
from medium.models import Medium
from blog.models import Title

class GalleryMediaDescription(View):
	def post(self, request, mid=None):
		mediaInfo=eval(request.body)
		mid, description=mediaInfo['mid'], mediaInfo['description']
		media=Medium.objects.get(id=mid)
		media.description=description
		media.save()
		return JsonResponse({'galleryMediaDescription':True})

class GalleryMediaDelete(View):
	def post(self, request, mid=None):
		mid=eval(request.body)['mid']
		media=Medium.objects.get(id=mid)
		media.delete()
		return JsonResponse({'GalleryMediaDeleted':True})

class GalleryPagination(View):
	def post(self, request):
		galleries, gid=tuple(), eval(request.body)['gid']
		gid, idRange, count=int(gid), 5, 0
		while not galleries:
			gid, galleries=fetchData(gid, idRange)
			idRange+=5
			if gid<2:break
		tmpl=loader.get_template('gallery-pagination.html')
		ctx=tmpl.render({'galleries':galleries}, request)
		data={'newData':ctx}
		return JsonResponse(data)

class GalleryDelete(View):
	def post(self, request):
	#def post(self, request, bid=None):
		gid=eval(request.body)['gid']
		gallery=Gallery.objects.get(id=gid)
		gallery.delete()
		return JsonResponse({'galleryDeleted':True})

class GalleryEdit(View):
	'''
	def get(self, request, gid=None):
		gallery=Gallery.objects.get(id=gid)
		return TemplateResponse(request, 'gallery-edit.html', {'gallery':gallery})
		return render(request, 'gallery-edit.html', {'gallery':gallery})
	'''
	def post(self, request):
		me, rqstPst=request.user, request.POST
		gid=int(rqstPst['gid'])
		title, gallery=rqstPst['title'], Gallery.objects.get(id=gid)
		galleryTitle=gallery.title
		if title!=galleryTitle.title:
			galleryTitle.title=title
			galleryTitle.save()
		for media in request.FILES.getlist('pics'):
			content_type=media.content_type
			if content_type in ['image/jpeg', 'image/png', 'image/gif']:
				gallery.picture.create(media=media)
		return JsonResponse({'galleryUpdated':True})
		return render(request, 'gallery-edit.html', {'gallery':gallery})

class GalleryAdd(View):
	def get(self, request):
		return render(request, 'gallery-add.html')
	def post(self, request):
		#me, pics=request.user, request.FILES['pics']
		me, title=request.user, request.POST['title']
		title=Title.objects.create(title=title)
		gallery=me.galler_gallery.create(title=title)
		timestamp, title, ggid, gid=gallery.timestamp, gallery.title.title, gallery.galler_id, gallery.id
		for media in request.FILES.getlist('pics'):
			content_type=media.content_type
			if content_type in ['image/jpeg', 'image/png', 'image/gif']:
				gallery.picture.create(media=media)
				#gallery.picture.add(media)
		tmpl=loader.get_template('gallery-template.html')
		ctx=tmpl.render({'gallery':gallery, 'medium':gallery.picture.all(), 'timestamp':timestamp, 'title':title, 'ggid':ggid, 'gid':gid})
		return JsonResponse({'galleryAdded':True, 'ctx':ctx})
		#HTTP_REFERER=request.META['HTTP_REFERER']HTTP_REFERER)
		#mime_type=magic_file(full_path, mime=True)
		#return HttpResponseRedirect(reverse('avatar-add'))

def fetchData(gid, idRange):
		qsFunc, galleries, count=Gallery.objects.filter, tuple(), 0
		while count<idRange:
			gid-=1
			querySet=qsFunc(id=gid)
			if querySet.exists():
				galleries+=(querySet.get(), )
				idRange-=1
			count+=1
		return gid, galleries

class Galleries(View):
	def get(self, request):
		me=request.user
		galleryQueryset=me.galler_gallery.filter(galler_id__isnull=False)
		if not galleryQueryset.exists():return render(request, 'galleries.html')
		latest_gallery, idRange, count=galleryQueryset.latest('timestamp'), 5, 0
		gid, galleries=latest_gallery.id, tuple()
		while not galleries:
			gid, galleries=fetchData(gid, idRange)
			if gid<2:break
		galleries=(latest_gallery, )+galleries
		return render(request, 'galleries.html', {'galleries':galleries})

class GalleryDetail(View):
	def get(self, request, gid=None):
		try:
			gallery=Gallery.objects.get(id=gid)
			userID, gallerID=request.user.id, gallery.galler_id
			approved=gallerID==userID
			return render(request, 'gallery-detail.html', {'gallery':gallery, 'medium':gallery.picture.all(), 'userID':userID, 'title':gallery.title.title, 'approved':approved, 'gid':gid})
		except: raise Http404('Query Not Found')

'''
class Gallery(View):
	def get(self, request):
		return render(request, 'gallery.html')
'''
