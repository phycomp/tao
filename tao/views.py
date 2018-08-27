from django.shortcuts import render
from django.views import View
from django.template import loader
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from .models import Contact
from post.models import Post

WEBMASTER=settings.WEBMASTER

def SendEmail(subject=None, body=None, receipts=None, webmaster=WEBMASTER):
	send_mail(subject, body, webmaster, receipts, fail_silently=False)

class AddCreditCard(View):
	def post(self, request, pid=None):
		pid=eval(request.body)['pid']
		pid, posts, idRange=int(pid), tuple(), 5
		while idRange:
			pid-=1
			posts+=(Post.objects.get(id=pid), )
			idRange-=1
		tmpl=loader.get_template('home-pagination.html')
		ctx=tmpl.render({'posts':posts}, request)
		data={'newData':ctx}
		return JsonResponse(data)

def fetchData(pid, idRange):
		qsFunc, posts, count=Post.objects.filter, tuple(), 0
		while count<idRange:
			pid-=1
			querySet=qsFunc(id=pid)
			if querySet.exists():
				posts+=(querySet.get(), )
				idRange-=1
			count+=1
		return pid, posts

class HomePagination(View):
	def post(self, request, pid=None):
		pid=eval(request.body)['pid']
		pid, posts, idRange=int(pid), tuple(), 5
		while not posts:
			pid, posts=fetchData(pid, idRange)
			idRange+=5
			if pid<2:break
		tmpl=loader.get_template('home-pagination.html')
		ctx=tmpl.render({'posts':posts}, request)
		return JsonResponse({'newData':ctx, 'userID':request.user.id})
		#posts=[Post.objects.get(id=pid) for pid in range(latestID-idRange, latestID)]

class HOME(View):
	def get(self, request):
		qs=Post.objects
		if not qs.exists():return render(request, 'home.html')
		latest_post, idRange, count=qs.latest('timestamp'), 5, 0
		pid, posts=latest_post.id, tuple()
		while not posts:
			pid, posts=fetchData(pid, idRange)
			idRange+=5
			if pid<2:break
		posts=(latest_post, )+posts
		return render(request, 'home.html', {'posts':posts, 'userID':request.user.id})
		#latest_posts=[Post.objects.get(id=pid) for pid in range(latestID-idRange, latestID)]
	def post(self, request):
		me, rqstPst=request.user, request.POST
		body=rqstPst['body']
		post=me.author_post.create(body=body)
		for media in request.FILES.getlist('attached'):
			medium=me.user_medium.create(media=media)
			post.media.add(medium)
		tmpl=loader.get_template('home-template.html')
		ctx=tmpl.render({'post':post}, request)
		return JsonResponse(dict(homePosted=True, ctx=ctx))

class ContactView(View):
	def get(self, request): return render(request, 'contact.html')
	def post(self, request):
		rqstPst=request.POST
		email, subject, body=rqstPst['email'], rqstPst['subject'], rqstPst['body']
		contact=Contact.objects.create(email=email, subject=subject, body=body)
		SendEmail(subject=subject, body=body, webmaster=WEBMASTER, receipts=[email])
		return JsonResponse({'ContactSent':True})

'''
def render_template(request, template='member-template.html', data=None):
		tmpl=loader.get_template(template)
		return tmpl.render(data, request)
'''
