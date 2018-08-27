from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views import View
from django.template import loader
from django.template.response import TemplateResponse

#from magic import from_file as magic_file
from .models import GoodsExchange
#from member.models import BlogBase
from medium.models import Medium
from gallery.models import Gallery

class GoodsExchangeMediaDescription(View):
	def post(self, request, mid=None):
		mediaInfo=eval(request.body)
		mid, description=mediaInfo['mid'], mediaInfo['description']
		media=Medium.objects.get(id=mid)
		media.description=description
		media.save()
		return JsonResponse({'goodsExchangeMediaDescription':True})

class GoodsExchangeMediaDelete(View):
	def post(self, request, mid=None):
		mid=eval(request.body)['mid']
		media=Medium.objects.get(id=mid)
		media.delete()
		return JsonResponse({'goodsExchangeMediaDeleted':True})

class GoodsExchangePagination(View):
	def post(self, request):
		GEs, geID=tuple(), eval(request.body)['geID']
		geID, idRange, count=int(geID), 5, 0
		while not GEs:
			geID, GEs=fetchData(geID, idRange)
			idRange+=5
			if geID<2:break
		tmpl=loader.get_template('ge-pagination.html')
		ctx=tmpl.render({'GEs':GEs}, request)
		data={'newData':ctx}
		return JsonResponse(data)

class GoodsExchangeDelete(View):
	def post(self, request):
		geID=eval(request.body)['geID']
		ge=GoodsExchange.objects.get(id=geID)
		ge.delete()
		return JsonResponse({'goodsExchangeDeleted':True})

class GoodsExchangeEdit(View):
	def get(self, request, gid=None):
		ge=GoodsExchange.objects.get(id=gid)
		return TemplateResponse(request, 'ge-edit.html', {'ge':ge})
		return render(request, 'ge-edit.html', {'ge':ge})
	def post(self, request, gid=None):
		me, rqstPst=request.user, request.POST
		title, ge=rqstPst['title'], GoodsExchange.objects.get(id=gid)
		gallery=ge.gallery
		for media in request.FILES.getlist('pics'):
			content_type=media.content_type
			if content_type in ['image/jpeg', 'image/png', 'image/gif']:
				gallery.picture.create(media=media)
				#ge.picture.add(media)
		#if title!=ge.title: if body != ge.body:
		geRevised=title!=ge.gallery.title
		#geRevised=True if title!=ge.title or body!=ge.body else False
		if geRevised:
			ge.title=title
			ge.save()
		return render(request, 'ge-edit.html', {'ge':ge})

class GoodsExchangeInvoke(View):
	#def get(self, request): return render(request, 'ge-add.html')
	def post(self, request):
		me, rqstPst=request.user, request.POST
		title, coordinate, date, time=rqstPst['title'], rqstPst['coordinate'], rqstPst['date'], rqstPst['time']
		#title, datetime=BlogBase.objects.create(title=title), ' '.join([date, time])
		gallery=me.galler_gallery.create(title=title)
		ge=gallery.gallery_goodsexchange.create(coordinate=coordinate, datetime=datetime)
		for media in request.FILES.getlist('pics'):
			content_type=media.content_type
			if content_type in ['image/jpeg', 'image/png', 'image/gif']:
				gallery.picture.create(media=media)
				#ge.picture.add(media)
		tmpl=loader.get_template('ge-template.html')
		ctx=tmpl.render({'ge':ge})
		return JsonResponse({'goodsExchangeInvoked':True, 'ctx':ctx})
		#HTTP_REFERER=request.META['HTTP_REFERER']HTTP_REFERER)
		#mime_type=magic_file(full_path, mime=True)

class GoodsExchangeApply(View):
	def get(self, request, gid=None):
		ge=GoodsExchange.objects.get(id=gid)
		return render(request, 'ge-apply.html', {'ge':ge})

class GoodsExchangeStatus(View):
	def post(self, request):
		me, geid=request.user, request.POST['geid']
		oriGE=GoodsExchange.objects.get(id=geid)
		#gallery=me.gallery_goodsexchange.create()
		gallery=me.galler_gallery.create()
		ge=GoodsExchange.objects.create(ge2ge=oriGE, gallery=gallery)
		#ge=me.launcher_goodsexchange.create(ge2ge=ge)
		#ge.gallery=gallery
		#title, coordinate, date, time=rqstPst['title'], rqstPst['coordinate'], rqstPst['date'], rqstPst['time']
		#title=BlogBase.objects.create(title=title)
		#gallery=Gallery.objects.create(title=title)
		#datetime=' '.join([date, time])
		#ge=me.launcher_goodsexchange.create(gallery=gallery, coordinate=coordinate, datetime=datetime)
		for media in request.FILES.getlist('pics'):
			content_type=media.content_type
			if content_type in ['image/jpeg', 'image/png', 'image/gif']:
				gallery.picture.create(media=media)
				#ge.picture.add(media)
		tmpl=loader.get_template('ge-template.html')
		ctx=tmpl.render({'ge':ge})
		return JsonResponse({'goodsExchangeApplied':True, 'ctx':ctx})
		#HTTP_REFERER=request.META['HTTP_REFERER']HTTP_REFERER)
		#mime_type=magic_file(full_path, mime=True)
		#return HttpResponseRedirect(reverse('avatar-add'))

def fetchData(geID, idRange):
		qsFunc, GEs, count=GoodsExchange.objects.filter, tuple(), 0
		while count<idRange:
			geID-=1
			querySet=qsFunc(id=geID)
			if querySet.exists():
				GEs+=(querySet.get(), )
				idRange-=1
			count+=1
		return geID, GEs

class GoodsExchanges(View):
	def get(self, request):
		me=request.user
		geQueryset=GoodsExchange.objects.filter(id__isnull=False)#me.launcher_goodsexchange.filter(launcher__isnull=False)
		if not geQueryset.exists():return render(request, 'goodsexchanges.html')
		latest_ge, idRange=geQueryset.latest('timestamp'), 5
		geID, GEs=latest_ge.id, tuple()
		while not GEs:
			geID, GEs=fetchData(geID, idRange)
			if geID<2: break
		GEs=(latest_ge, )+GEs
		return render(request, 'goodsexchanges.html', {'GEs':GEs})
		#perm===userID

class GoodsExchangeDetail(View):
	def get(self, request, gid=None):
		try:
			oriGE=GoodsExchange.objects.get(id=gid)
			ges=oriGE.goodsexchange_goodsexchange.filter(id__isnull=False).all()
			return render(request, 'ge-detail.html', {'oriGE':oriGE, 'ges':ges})
		except: raise Http404('Query Not Found')

class GoodsExchangeApprove(View):
	def post(self, request):
		geInfo=eval(request.body)
		print(geInfo)
		oriGEID, geID=geInfo['oriGEID'], geInfo['geID']
		oriGE=GoodsExchange.objects.get(id=oriGEID)
		ge=GoodsExchange.objects.get(id=geID)
		oriGE.isDealt=True
		ge.isDealt=True
		ge.save()
		oriGE.save()
		return JsonResponse({'goodsExchangeApproved':True})

'''
class GoodsExchange(View):
	def get(self, request):
		return render(request, 'ge.html')
'''
