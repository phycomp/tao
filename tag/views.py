from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Tag

class Tags(View):
	def get(self, request):
		tags=Tag.objects.all()
		return render(request, 'tags.html', {'tags':tags})

class TagDetail(View):
	def get(self, request, tid):
		tag=Tag.objects.get(id=tid)
		blogs=tag.tag_blog.all()
		return render(request, 'tag-detail.html', {'tag':tag, 'blogs':blogs})

class TagAdd(View):
	def post(self, request):
		me, rqstPst=request.user, request.POST
		tag=rqstPst['tag']
		#print(loads(request.body))	#__dict__)	#._body)
		#bodyinfo=dump(request.body)	#eval(request._body)
		#print(bodyinfo['textareaData'], bodyinfo['title'], )
		tag=Tag.objects.create(tag=tag)
		#blog=Blog.objects.create(body='kdjlkfjd\n', title='BLOG TITLE', post_ptr=post, author=u)
		#medium=blog.post_ptr.media.create()
		return JsonResponse(dict(TagAdded=True))
