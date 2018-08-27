from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse, Http404
from django.template import loader
from .models import Sutra, CommentSutra
from book.models import Book, Chapter
from post.views import postMediaAdd

class SutraCommentSelfDelete(View):
	def post(self, request):
		cid=eval(request.body)['cid']
		CommentSutra.objects.get(id=cid).delete()
		return JsonResponse({'commentSutraSelfDelete':True})

class SutraCommentSelfEdit(View):
	def post(self, request):
		scInfo=eval(request.body)
		cid, body=scInfo['cid'], scInfo['body']
		commentsutra=CommentSutra.objects.get(id=cid)
		commentsutra.body=body
		commentsutra.save()
		return JsonResponse({'commentSutraSelfEdit':True})

class SutraCommentEdit(View):
	def post(self, request):
		sutraComment=eval(request.body)
		cid, body=sutraComment['cid'], sutraComment['body']
		commentsutra=CommentSutra.objects.get(id=cid)
		if commentsutra.body!=body:
			commentsutra.body=body
			commentsutra.save()
			return JsonResponse({'commentSutraEdit':True})
		return JsonResponse({'commentSutraEdit':False})

class SutraCommentDelete(View):
	def post(self, request):
		cid=eval(request.body)['cid']
		CommentSutra.objects.get(id=cid).delete()
		return JsonResponse({'commentSutraDelete':True})

class SutraCommentSelf(View):
	def post(self, request):
		me, sutraInfo=request.user, eval(request.body)
		cid, sid, body=sutraInfo['cid'], sutraInfo['sid'], sutraInfo['body']
		comment_sutra_self=me.commentor_sutra.create(commentsutra_id=cid, body=body, sutra_id=sid)
		tmpl=loader.get_template('sutra-comment-self.html')
		ctx=tmpl.render({'comment':comment_sutra_self}, request)
		return JsonResponse({'ctx':ctx, 'commentSutraSelf':True})

class SutraComment(View):
	def post(self, request):
		me, rqstPst=request.user, request.POST
		sid, body=rqstPst['sid'], rqstPst['body']
		#sutra=Sutra.objects.get(id=sid)
		#post=me.author_post.create(body=body)
		#postMediaAdd(me, post, request.FILES.getlist('attached'))
		comment_sutra=me.commentor_sutra.create(body=body, sutra_id=sid)
		tmpl=loader.get_template('sutra-comment-template.html')
		ctx=tmpl.render({'comment':comment_sutra, 'sid':sid}, request)
		return JsonResponse({'ctx':ctx, 'commentSutraPosted':True})

class SutraBookChapter(View):
	def get(self, request, bid=None, cid=None):
		chapter=Chapter.objects.get(id=cid)
		#data, book, chapter={}, Book.objects.get(id=bid), Chapter.objects.get(id=cid)
		#data['book'], data['chapter']=book, chapter
		sutras=chapter.chapter_sutra.order_by('timestamp').all()
		return render(request, 'sutra-book-chapter.html', {'chapter':chapter, 'sutras':sutras})

class SutraBook(View):
	def get(self, request, bid=None):
		book=Book.objects.get(id=bid)
		return render(request, 'sutra-book.html', {'book':book})

class Sutras(View):
	def get(self, request):
		return render(request, 'sutras.html', {'books':Book.objects.all()})

class SutraDetail(View):
	def get(self, request, sid=None):
		try:
			data, sutra={}, Sutra.objects.get(id=sid)
			comments=sutra.sutra_commentsutra.filter(commentsutra=None).all()
			data['sutra'], data['comments']=sutra, comments
			return render(request, 'sutra-detail.html', {'sid':sid, 'sutra':sutra, 'comments':comments, 'userID':request.user.id})
		except: raise Http404('Forum Not Found')

class SutraEdit(View):
	def get(self, request, sid=None):
		data, sutra={}, Sutra.objects.get(id=sid)
		data['sutra']=sutra
		return render(request, 'sutra_edit.html', data)
	def post(self, request, sid=None):
		me, rqstPst=request.user, request.POST
		title, body=rqstPst['title'], rqstPst['body']
		sutra=Sutra.objects.get(id=sid)
		if title!=sutra.title and body!=sutra.body: sutra.title=title; sutra.body=body; sutra.save()
		#Susid
		#=me, title=title, body=body)
		return render(request, 'sutra_edit.html')

'''
class SutraAdd(View):
	def get(self, request):
		return render(request, 'sutra_add.html')
	def post(self, request):
		me, rqstPst=request.user, request.POST
		title, body=rqstPst['title'], rqstPst['body']
		Sutra.objects.create(author=me, title=title, body=body)
		return render(request, 'sutra_add.html')

class SutraSection(View):
	def get(self, request, sid=None):
		data, section={}, Sutra.objects.get(id=sid)
		data['section']=section
		return render(request, 'sutra-section.html', data)
'''
