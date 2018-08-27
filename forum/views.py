from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse, Http404
from django.views import View
from django.template import loader
from django.template.response import TemplateResponse
from medium.models import Medium
from post.models import Post
from post.views import postMediaAdd
from blog.models import Title
from .models import Forum

class ForumPagination(View):
	def post(self, request, pid=None):
		forumInfo=eval(request.body)
		fid, forums, idRange, count=int(forumInfo['fid']), tuple(), 5, 0
		while count<idRange:
			fid-=1
			querySet=Forum.objects.filter(id=fid)
			if querySet.exists():
				forums+=(querySet.get(), )
				idRange-=1
			count+=1
		tmpl=loader.get_template('forum-pagination.html')
		ctx=tmpl.render({'forums':forums}, request)
		return JsonResponse({'newData':ctx})
		#posts=[Post.objects.get(id=pid) for pid in range(latestID-idRange, latestID)]

class ForumContextEdit(View):
	def post(self, request, fid=None):
		me, forumInfo=request.user, eval(request.body)
		fid, body=forumInfo['fid'], forumInfo['body']
		forum=Forum.objects.get(id=fid)
		post=forum.post
		#forumRevised=True if title!=forum.title or body!=forum.body else False
		if body!=post.body:
			post.body=body
			forum.save()
		return JsonResponse(dict(forumCtxEdited=True))

class ForumReply(View):
	def post(self, request):
		me, rqstPst=request.user, request.POST
		fid, body=rqstPst['fid'], rqstPst['body']
		oldForum=Forum.objects.get(id=fid)
		post=me.author_post.create(body=body)
		FILES=request.FILES.getlist('attached')
		if FILES: postMediaAdd(me, post, FILES)
		forum_reply=oldForum.selv_forum.create(post=post)
		tmpl=loader.get_template('forum-reply.html')
		ctx=tmpl.render({'forum_reply':forum_reply}, request)
		return JsonResponse({'ctx':ctx, 'forumReply':True})
		#forum, commentor=comment_forum.forum, comment_forum.commentor
		#comment_forum_self=comment_forum.commentforum_commentforum.create(commentforum=comment_forum, commentor=commentor, body=body, forum=forum)

class ForumSelf(View):
	def post(self, request):
		me, rqstPst=request.user, request.POST
		fid, title, body=rqstPst['fid'], rqstPst['title'], rqstPst['body']
		title=Title.objects.create(title=title)
		oldForum=Forum.objects.get(id=fid)
		post=me.author_post.create(body=body)	#Post.objects.create(author=me)
		FILES=request.FILES.getlist('attached')
		if FILES: postMediaAdd(me, post, FILES)
		forum_self=oldForum.selv_forum.create(post=post, title=title)
		tmpl=loader.get_template('forum-self.html')
		ctx=tmpl.render({'forum':forum_self}, request)
		return JsonResponse({'ctx':ctx, 'forumSelf':True})
		#forum, commentor=comment_forum.forum, comment_forum.commentor
		#comment_forum_self=comment_forum.commentforum_commentforum.create(commentforum=comment_forum, commentor=commentor, body=body, forum=forum)

class ForumSelfDelete(View):
	def post(self, request):
		fid=eval(request.body)['fid']
		Forum.objects.get(id=fid).delete()
		return JsonResponse(dict(forumSelfDelete=True))

class ForumSelfEdit(View):
	def post(self, request):
		fseInfo=eval(request.body)
		fid, body=fseInfo['fid'], fseInfo['body']
		forum=Forum.objects.get(id=fid)
		post=forum.post
		if post.body!=body:
			post.body=body
			post.save()
			return JsonResponse({'forumSelfEdit':True})
		return JsonResponse({'forumSelfEdit':False})

class ForumMediaDelete(View):
	def post(self, request, mid=None):
		midInfo=eval(request.body)
		mid=midInfo['mid']
		media=Medium.objects.get(id=mid)
		media.delete()
		return JsonResponse({'ForumMediaDeleted':True})

class ForumReplyEdit(View):
	def post(self, request):
		fcInfo=eval(request.body)
		fid, body=fcInfo['fid'], fcInfo['body']
		forum=Forum.objects.get(id=fid)
		post=forum.post
		if post.body!=body:
			post.body=body
			post.save()
			return JsonResponse({'forumReplyEdit':True})
		return JsonResponse({'forumReplyEdit':False})

class ForumReplyDelete(View):
	def post(self, request):
		fid=eval(request.body)['fid']
		Forum.objects.get(id=fid).delete()
		return JsonResponse(dict(forumReplyDelete=True))

class ForumDetail(View):
	def get(self, request, fid=None):
			forum=Forum.objects.get(id=fid)
			userID, forumerID=request.user.id, forum.forumerID
			approved=forumerID==userID
			#selves=forum.forum_forum.filter(Q(self__isnull=False)|Q(title__isnull=True)).all()
			selves=forum.selv_forum.all()
			#data['forum'], data['selves']=forum, selves
			return render(request, 'forum-detail.html', {'medium':forum.post.media.all(), 'timestamp':forum.timestamp, 'title':forum.title.title, 'body':forum.post.body, 'approved':approved, 'forumerID':forumerID, 'userID':userID, 'fid':fid, 'forum':forum, 'selves':selves})

class ForumEdit(View):
	'''
	def get(self, request, fid=None):
		data, forum={}, Forum.objects.get(id=fid)
		data['forum']=forum
		return TemplateResponse(request, 'forum-edit.html', {'forum':forum})
		return render(request, 'forum-edit.html', data)
	'''
	def post(self, request):
		me, rqstPst=request.user, request.POST
		fid, title, body=rqstPst['fid'], rqstPst['title'], rqstPst['body']
		forum=Forum.objects.get(id=fid)
		post, forumTitle=forum.post, forum.title
		FILES=request.FILES.getlist('attached')
		if FILES: postMediaAdd(me, post, FILES)
		forumBody=post.body
		titleRevised, bodyRevised=title!=forumTitle.title, body!=forumBody
		if titleRevised:
			forumTitle.title=title
			forumTitle.save()
		if bodyRevised:
			post.body=body
			post.save()
		if bodyRevised or titleRevised: return JsonResponse({'forumUpdated':True})
		return JsonResponse({'forumUpdated':False})

def fetchData(fid, idRange):
		qsFunc, forums, count=Forum.objects.filter, tuple(), 0
		while count<idRange:
			fid-=1
			querySet=qsFunc(id=fid)
			if querySet.exists():
				forums+=(querySet.get(), )
				idRange-=1
			count+=1
		return fid, forums

class Forums(View):
	def get(self, request):
		data, me, qs={}, request.user, Forum.objects.filter(id__isnull=False)
		if not qs.exists(): return render(request, 'forums.html')
		latest_forum, idRange=qs.latest('timestamp'), 5
		fid, forums=latest_forum.id, tuple()
		while not forums:
			fid, forums=fetchData(fid, idRange)
			idRange+=5
		forums=(latest_forum, )+forums
		return render(request, 'forums.html', {'forums':forums, 'userID':request.user.id})
		return TemplateResponse(request, 'forums.html', {'forums':forums})
		data['forums']=Forum.objects.filter(Q(selv__isnull=True)|Q(title__isnull=False)).all()
		#author, author_id, forum, body, created, id, media, post_commentpost, post_forum, sutra, wallpost
		#posts=me.author_post.filter(forum__isnull=False)
		#forums=[post.forum for post in posts]
		#data=dict(forums=forums)
		return render(request, 'forums.html', data)

class ForumAdd(View):
	#def get(self, request): return render(request, 'forum-template.html')
	def post(self, request):
		me, rqstPst=request.user, request.POST
		title, body=rqstPst['title'], rqstPst['body']
		title=Title.objects.create(title=title)
		post=me.author_post.create(body=body)
		FILES=request.FILES.getlist('attached')
		if FILES: postMediaAdd(me, post, FILES)
		forum=post.post_forum.create(title=title)	#Forum.objects.create(post=post)
		tmpl=loader.get_template('forum-template.html')
		ctx=tmpl.render({'forum':forum}, request)
		return JsonResponse({'forumAdded':True, 'ctx':ctx})
		#medium=forum.post_ptr.media.create()

class ForumDelete(View):
	def post(self, request):
		fidInfo=eval(request.body)
		fid=fidInfo['fid']
		forum=Forum.objects.get(id=fid)
		forum.delete()
		return JsonResponse({'ForumDeleted':True})

'''
class ForumComment(View):
	#def get(self, request): return render(request, 'forum-add.html')
	def post(self, request):
		me, mdm, rqstPst=request.user, [], request.POST
		fid, title, body=rqstPst['fid'], rqstPst['title'], rqstPst['body']
		forum=Forum.objects.get(id=fid)
		commentforum=forum.forum_commentforum.create(body=body, title=title, commentor=me)
		post=me.author_post.create(body=body)
		forum=post.post_forum.create(title=title)	#Forum.objects.create(post=post)
		#forum=Forum.objects.create(body='kdjlkfjd\n', title='BLOG TITLE', post_ptr=post, author=u)
		#medium=forum.post_ptr.media.create()
		for post_media in request.FILES.getlist('attached'):
			media=me.user_medium.create(media=post_media)
			mdm.append(media)
		post.media.add(mdm)
		ctx=render_template(forum, template_name='forum-template.html')
		return JsonResponse(dict(forumAdded=True, ctx=ctx))

class ForumComment(View):
	def post(self, request):
		me, fcInfo=request.user, eval(request.body)	#request.POST['body']
		fid, body=fcInfo['fid'], fcInfo['body']
		forum=Forum.objects.get(id=fid)
		comment_forum=forum.forum_commentforum.create(body=body, commentor=me)
		#comment_sutra=sutra.sutra_commentsutra.create(body=body, commentor=me, commentsutra=sutra)
		tmpl=loader.get_template('forum-comment-template.html')
		ctx=tmpl.render({'comment':comment_forum})
		return JsonResponse(dict(ctx=ctx, commentForumPosted=True))

'''
