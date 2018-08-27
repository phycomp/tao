from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse, Http404
from django.contrib.auth import get_user_model
from django.views import View
from django.urls import reverse
from django.template import loader
from django.template.response import TemplateResponse

#from django.utils.timezone import now
from json import loads, dump
from tag.models import Tag
from post.models import Post
from post.views import postMediaAdd
from .models import Blog, CommentBlog, Title
from medium.models import Medium
User=get_user_model()
#now=now()

class BlogPagination(View):
	def post(self, request):
		bid=eval(request.body)['bid']
		bid, blogs, idRange, count=int(bid), tuple(), 5, 0
		while not blogs:
			bid, blogs=fetchData(bid, idRange)
			idRange+=5
			if bid<2:break
		tmpl=loader.get_template('blog-pagination.html')
		ctx=tmpl.render({'blogs':blogs}, request)
		return JsonResponse({'newData':ctx})
		#blogs=[Post.objects.get(id=pid) for pid in range(latestID-idRange, latestID)]

class BlogCommentSelfEdit(View):
	def post(self, request):
		bcInfo=eval(request.body)
		selvID, body=bcInfo['selvID'], bcInfo['body']
		commentblog=CommentBlog.objects.get(id=selvID)
		commentblogBody=commentblog.body
		if commentblogBody!=body:
			commentblog.save()
			return JsonResponse({'commentBlogSelfEdit':True})
		return JsonResponse({'commentBlogSelfEdit':False})

class BlogCommentSelfDelete(View):
	def post(self, request):
		selvID=eval(request.body)['selvID']
		CommentBlog.objects.get(id=selvID).delete()
		return JsonResponse({'commentBlogSelfDelete':True})

class BlogCommentEdit(View):
	def post(self, request):
		bcInfo=eval(request.body)
		cid, body=bcInfo['cid'], bcInfo['body']
		commentblog=CommentBlog.objects.get(id=cid)
		commentblogBody=commentblog.body
		if commentblogBody!=body:
			commentblog.body=body
			commentblog.save()
			return JsonResponse({'commentBlogEdited':True})
		return JsonResponse({'commentBlogEdited':False})

class BlogCommentDelete(View):
	def post(self, request):
		cid=eval(request.body)['cid']
		CommentBlog.objects.get(id=cid).delete()
		return JsonResponse({'commentBlogDelete':True})

class BlogCommentSelf(View):
	def post(self, request):
		me, blogInfo=request.user, eval(request.body)
		cid, bid, body=blogInfo['cid'], blogInfo['bid'], blogInfo['body']
		comment_blog_self=me.commentor_commentblog.create(commentblog_id=cid, body=body, blog_id=bid)
		tmpl=loader.get_template('blog-comment-self.html')
		ctx=tmpl.render({'selv':comment_blog_self, 'approved':True}, request)
		return JsonResponse({'ctx':ctx, 'commentBlogSelfed':True})

def fetchData(bid, idRange):
		qsFunc, blogs, count=Blog.objects.filter, tuple(), 0
		while count<idRange:
			bid-=1
			querySet=qsFunc(id=bid)
			if querySet.exists():
				blogs+=(querySet.get(), )
				idRange-=1
			count+=1
		return bid, blogs

class Blogs(View):
	def get(self, request):
		blogQueryset=Blog.objects.filter(id__isnull=False)
		if not blogQueryset.exists(): return render(request, 'blogs.html')
		latest_blog, idRange, count=blogQueryset.latest('timestamp'), 5, 0
		bid, blogs=latest_blog.id, tuple()
		while not blogs:
			bid, blogs=fetchData(bid, idRange)
			idRange+=5
			if bid<2:break
		blogs=(latest_blog, )+blogs
		return render(request, 'blogs.html', {'blogs':blogs})
		#latest_blogs=[Post.objects.get(id=pid) for pid in range(latestID-idRange, latestID)]

class BlogDetail(View):
	def get(self, request, bid=None):
		try:
			userID, blog=request.user.id, Blog.objects.get(id=bid)
			bloggerID, comments=blog.bloggerID, blog.blog_commentblog.filter(commentblog=None).all()
			#data['blog'], data['comments']=blog, comments
			approved, tags=userID==bloggerID, blog.tag.all()
			return render(request, 'blog-detail.html', {'bid':bid, 'comments':comments, 'tags':tags, 'bloggerID':bloggerID,'approved':approved, 'medium':blog.post.media.all(), 'title':blog.title.title, 'body':blog.post.body, 'timestamp':blog.timestamp, })
		except: raise Http404('Query not found.')

class BlogContextEdit(View):
	def post(self, request, bid=None):
		blogInfo=eval(request.body)
		bid, body=blogInfo['bid'], blogInfo['body']
		blog=Blog.objects.get(id=bid)
		blogBody=blog.body
		if body!=blogBody:
			blog.body=body
			blog.save()
			return JsonResponse({'blogCtxEdited':True})
		return JsonResponse({'blogCtxEdited':False})

class BlogMediaDelete(View):
	def post(self, request, mid=None):
		midinfo=eval(request.body)
		mid=midinfo['mid']
		media=Medium.objects.get(id=mid)
		media.delete()
		return JsonResponse({'BlogMediaDeleted':True})

class BlogEdit(View):
	'''
	def get(self, request, bid=None):
		data, blog={}, Blog.objects.get(id=bid)
		data['blog']=blog
		return TemplateResponse(request, 'blog-edit.html', data)
		return render(request, 'blog-edit.html', data)
	'''
	def post(self, request):
		me, rqstPst=request.user, request.POST
		bid, title, body=rqstPst['bid'], rqstPst['title'], rqstPst['body']
		blog=Blog.objects.get(id=bid)
		post, blogTitle=blog.post, blog.title
		FILES=request.FILES.getlist('attached')
		if FILES: postMediaAdd(me, post, FILES)
		titleRevised, bodyRevised=title!=blogTitle.title, body!=post.body
		if titleRevised:
			blogTitle.title=title
			blogTitle.save()
		if bodyRevised:
			post.body=body
			post.save()
		if bodyRevised or titleRevised: return JsonResponse({'blogUpdated':True})
		return JsonResponse({'blogUpdated':False})

class BlogSearch(View):
	def post(self, request, mid=None):
		pttrninfo=eval(request.body)
		pttrn=pttrninfo['q']
		#blogs=Blog.objects.filter(created__lte=now)
		blogs=Blog.objects.filter(body__contains=pttrn)
		return render(request, 'search-template.html', {'blogs':blogs})

class BlogDelete(View):
	def post(self, request):
		bid=eval(request.body)['bid']
		blog=Blog.objects.get(id=bid)
		blog.delete()
		return JsonResponse({'blogDeleted':True})

class BlogComment(View):
	def post(self, request):
		me, bcInfo=request.user, eval(request.body)
		bid, body=bcInfo['bid'], bcInfo['body']
		#blog=Blog.objects.get(id=bid)
		comment_blog=me.commentor_commentblog.create(blog_id=bid, body=body)
		#comment_blog=blog.blog_commentblog.create(body=body, commentor=me)
		tmpl=loader.get_template('blog-comment-template.html')
		ctx=tmpl.render({'comment':comment_blog, 'bid':bid}, request)
		return JsonResponse({'ctx':ctx, 'blogCommented':True})

class BlogAdd(View):
	#def get(self, request): return render(request, 'blog-add.html')
	def post(self, request):
		me, rqstPst=request.user, request.POST
		title, body=rqstPst['title'], rqstPst['body']
		post=me.author_post.create(body=body)
		title=Title.objects.create(title=title)
		blog=post.post_blog.create(title=title)
		FILES=request.FILES.getlist('attached')
		if FILES: postMediaAdd(me, post, FILES)
		'''
		for media in request.FILES.getlist('attached'):
			mdm=me.user_medium.create(media=media)
			post.media.add(mdm)
		'''
		tmpl=loader.get_template('blog-template.html')
		ctx=tmpl.render({'blog':blog}, request)
		return JsonResponse({'blogAdded':True, 'ctx':ctx})

