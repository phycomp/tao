from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse, Http404
from django.template import loader
from django.contrib.auth import get_user_model
from django.template import loader
from django.template.response import TemplateResponse
from medium.models import Medium
from .models import Post, CommentPost, WallPost
User=get_user_model()

def postMediaAdd(me, post, FILES):
		for media in FILES:
			medium=me.user_medium.create(media=media)
			post.media.add(medium)

class WallAdd(View):
	def post(self, request):
		rqstPst=request.POST
		me, oid, body=request.user, rqstPst['oid'], rqstPst['body']
		post=me.author_post.create(body=body)
		FILES=request.FILES.getlist('attached')
		if FILES: postMediaAdd(me, post, FILES)
		wall_post=post.post_wallpost.create(waller_id=oid)
		#other=User.objects.get(id=)
		#other.waller_wallpost.create(body=body, post_id=post.id)
		#WallPost.objects.create(waller=other, author=me, body=body, post_ptr=post)
		tmpl=loader.get_template('wall-template.html')
		ctx=tmpl.render({'post':post}, request)
		return JsonResponse({'wallPosted':True, 'ctx':ctx})

class PostContextEdit(View):
	def post(self, request, bid=None):
		me, postInfo=request.user, eval(request.body)
		pid, body=postInfo['pid'], postInfo['body']
		post=Post.objects.get(id=pid)
		if body!=post.body:
			post.body=body
			post.save()
			return JsonResponse({'postCtxEdited':True})
		return JsonResponse({'postCtxEdited':False})

class PostCommentEdit(View):
	def post(self, request):
		pcInfo=eval(request.body)
		cid, body=pcInfo['cid'], pcInfo['body']
		commentpost=CommentPost.objects.get(id=cid)
		commentpostBody=commentpost.body
		if commentpostBody!=body:
			commentpost.body=body
			commentpost.save()
			return JsonResponse({'commentPostEdited':True})
		return JsonResponse({'commentPostEdited':False})

class PostCommentSelfEdit(View):
	def post(self, request):
		pcInfo=eval(request.body)
		selvID, body=pcInfo['selvID'], pcInfo['body']
		commentblog=CommentPost.objects.get(id=selvID)
		commentblogBody=commentblog.body
		if commentblogBody!=body:
			commentblog.body=body
			commentblog.save()
			return JsonResponse({'commentPostSelfEdited':True})
		return JsonResponse({'commentPostSelfEdited':False})

class PostCommentSelfDelete(View):
	def post(self, request):
		selvID=eval(request.body)['selvID']
		CommentPost.objects.get(id=selvID).delete()
		return JsonResponse(dict(commentPostSelfDelete=True))

class PostCommentSelf(View):
	def post(self, request):
		me, postInfo=request.user, eval(request.body)
		cid, pid, body=postInfo['cid'], postInfo['pid'], postInfo['body']
		#comment_post=CommentPost.objects.get(id=cid)
		#postID=comment_post.post_id
		selv=me.commentor_commentpost.create(commentpost_id=cid, body=body, post_id=pid)
		tmpl=loader.get_template('post-comment-self.html')
		ctx=tmpl.render({'selv':selv, 'userID':me.id}, request)
		return JsonResponse({'ctx':ctx, 'commentPostSelf':True})

class PostEdit(View):
	'''
	def get(self, request, pid=None):
		post=Post.objects.get(id=pid)
		return TemplateResponse(request, 'post-edit.html', {'post':post})
		return render(request, 'post-edit.html', {'post':post})
	'''
	def post(self, request):
		me, rqstPst=request.user, request.POST
		body, pid=rqstPst['body'], rqstPst['pid']
		post=Post.objects.get(id=pid)
		postBody=post.body
		FILES=request.FILES.getlist('attached')
		if FILES: postMediaAdd(me, post, FILES)
		if body!=postBody:
			post.body=body
			post.save()
			return JsonResponse({'postUpdated':True})
		return JsonResponse({'postUpdated':False})

class PostAdd(View):
	def post(self, request, pid=None):
		me, body=request.user, request.POST['body']
		userID, post=me.id, me.author_post.create(body=body)
		FILES=request.FILES.getlist('attached')
		if FILES: postMediaAdd(me, post, FILES)
		tmpl=loader.get_template('post-template.html')
		ctx=tmpl.render({'userID':userID, 'post':post}, request)
		return JsonResponse({'postUpdated':True, 'ctx':ctx})

class PostDetail(View):
	def get(self, request, pid=None):
		try:
			userID, post=request.user.id, Post.objects.get(id=pid)
			aid, comments=post.author_id, post.post_commentpost.filter(commentpost=None).all()
			approved=aid==userID
			#data['post'], data['comments']=post, comments
			return render(request, 'post-detail.html', {'medium':post.media.all(), 'pid':pid, 'aid':aid, 'userID':userID, 'post':post, 'body':post.body, 'approved':approved, 'comments':comments})
		except: raise Http404('Query not found.')

class PostMediaDelete(View):
	def post(self, request, mid=None):
		midinfo=eval(request.body)
		mid=midinfo['mid']
		media=Medium.objects.get(id=mid)
		media.delete()
		return JsonResponse({'PostMediaDeleted':True})

class PostDelete(View):
	def post(self, request):
		pid=eval(request.body)['pid']
		post=Post.objects.get(id=pid)
		post.delete()
		return JsonResponse({'PostDeleted':True})

class PostCommentDelete(View):
	def post(self, request):
		cid=eval(request.body)['cid']
		CommentPost.objects.get(id=cid).delete()
		return JsonResponse(dict(commentPostDelete=True))

class PostComment(View):
	def post(self, request):
		me, info=request.user, eval(request.body)
		pid, body=info['pid'], info['body']
		post=Post.objects.get(id=pid)
		comment_post=post.post_commentpost.create(body=body, commentor=me)
		#comment_sutra=sutra.sutra_commentsutra.create(body=body, commentor=me, commentsutra=sutra)
		tmpl=loader.get_template('post-comment-template.html')
		ctx=tmpl.render({'comment':comment_post}, request)
		return JsonResponse(dict(ctx=ctx, commentPosted=True))

