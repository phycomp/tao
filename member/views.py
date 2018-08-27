from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model, authenticate, logout as auth_logout, login as auth_login
from django.urls import reverse
from django.views import View	#, RedirectView
from django.db.models import Q
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import loader
#from django.template.response import TemplateResponse
from django.conf import settings
#from django.views.generic.edit import CreateView, UpdateView
#from django.views.generic.list import ListView
from random import choices

from PIL.Image import open as img_open
User=get_user_model()

from post.models import WallPost, Post
#from friend.models import Friend
from tao.views import SendEmail

def passwordResetEmail(receipts=None, random_password=None):
	subject, body='Password Reset', 'Your Password %s Reset.'%random_password
	if receipts:
		SendEmail(subject=subject, body=body, receipts=receipts)

def uniqueEmail(email=None):
	return True if User.objects.filter(email=email) else False
def uniqueCellular(cellular=None):
	return True if User.objects.filter(cellular=cellular) else False

class ProfilePagination(View):
	def post(self, request, pid=None):
		pid=eval(request.body)['pid']
		pid, posts, idRange=int(pid), tuple(), 5
		while not posts:
			pid, posts=fetchData(pid, idRange)
			idRange+=5
			if pid<2:break
		tmpl=loader.get_template('profile-pagination.html')
		ctx=tmpl.render({'posts':posts, 'userID':request.user.id}, request)
		return JsonResponse({'newData':ctx})
		#posts=[Post.objects.get(id=pid) for pid in range(latestID-idRange, latestID)]

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

class MePagination(View):
	def post(self, request, pid=None):
		pid=eval(request.body)['pid']
		pid, posts, idRange, count=int(pid), tuple(), 5, 0
		while not posts:
			pid, posts=fetchData(pid, idRange)
			idRange+=5
			if pid<2:break
		tmpl=loader.get_template('me-pagination.html')
		ctx=tmpl.render({'posts':posts}, request)
		return JsonResponse({'newData':ctx})

#class ME(LoginRequiredMixin, View):

class ME(View):
	def get(self, request):
		IDs, me, data, idRange, count=[], request.user, {}, 5, 0
		invokerQuery=me.user_friendship.filter(invoker_id__isnull=False)
		if invokerQuery.exists():
			IIDs=[friendship.invoker_id for friendship in invokerQuery][:5]
			#IIDs=choices(IIDs, k=5)
			data['IIDs']=IIDs
			IDs+=IIDs
		friendQuery=me.user_friendship.filter(friend_id__isnull=False)
		if friendQuery.exists():
			FIDs=[friendship.friend_id for friendship in friendQuery][:5]
			#FIDs=choices(FIDs, k=5)
			data.update({'FIDs':FIDs})
			IDs+=FIDs
		#if IIDs and FIDs:IDs=IIDs+FIDs
		otherQueryset=User.objects.exclude(identifier=me).exclude(id__in=IDs)
		if otherQueryset.exists():
			OIDs=[other.id for other in otherQueryset]	#[:5]
			OIDs=choices(OIDs, k=5)
			data.update({'OIDs':OIDs})
		postQueryset=me.author_post.filter(id__isnull=False)
		if not postQueryset.exists(): pass
		else:
			latest_post=postQueryset.latest('timestamp')
			pid, posts=latest_post.id, tuple()
			while not posts:
				pid, posts=fetchData(pid, idRange)
				idRange+=5
				if pid<2:break
			posts=(latest_post, )+posts
			data.update({'posts':posts})
		data.update({'userID':request.user.id})
		return render(request, 'me.html', data)
		#[invoker for invoker in Friend.objects.exclude(invoker=me)]
		#invokers=invokers.objects.all()
		#return render(request, 'me.html', data)
		data=dict(invokers=invokers, posts=posts, others=others)
		return TemplateResponse(request, 'me.html', dict(posts=posts, members=members))
		posts=request.user.author_post.filter(Q(blog__isnull=True)&Q(sutra__isnull=True))
		#data=dict(ajax_url=reverse('post-add'), redirect_url=reverse('me'), posts=posts)
		#user=User.objects.get(identifier=identifier)
		user=User.objects.get_by_natural_key(username=identifier)
		#identifier=request.post.get('identifier')

def checkUsername(username=None):
	#try: return User.objects.get_by_natural_key(username=username)
	#try: return 
	userQS=User.objects.filter(Q(identifier=username)|Q(email=username)|Q(cellular=username))
	return userQS.get() if userQS else None
	'''
	login_url = settings.LOGIN_URL
	redirect_field_name = 'redirect_to'
	try: return User.objects.get(Q(identifier=username)|Q(email=username)|Q(cellular=username))
	except: return None
	for item in request.POST.lists():
		if item: data, userinfo={}, eval(item[0])
	username, password=userinfo['username'], userinfo['password']
	try:
		user=User.objects.get_by_natural_key(username=username)
		data['UserExisted']=True if user.check_password(password) else False
	except: pass
	print(data)
		return JsonResponse(data)
	'''

class passwordForgot(View):
	def get(self, request): return render(request, 'password-forgot.html') 
	def post(self, request):
		data, rqstPst={}, request.POST
		#for item in request.POST.lists():
		#	if item: data, email={}, eval(item[0])
		email=rqstPst['email']
		qs=User.objects.filter(email=email)
		if qs:
			me, random_password=qs.get(), User.objects.make_random_password()
			me.set_password(random_password)
			me.save()
			data['UserExisted'], receipts=True, [me]
			passwordResetEmail(receipts=receipts, random_password=random_password)
		else: data['UserExisted']=False
		return JsonResponse(data)

def checkPasswordReset(request):
	#for item in request.POST.lists():
	#	if item: userinfo=eval(item[0])
	data, me, rqstPst={}, request.user, request.POST
	print(request.POST)
	old_password, password, Password=rqstPst['old_password'], rqstPst['password'], rqstPst['Password']
	print(old_password, password, Password)
	passwordEqual=password==Password
	#UserExisted=True if password and Password and password==Password else False
	data['passwordResetStatus']=me.check_password(old_password) and passwordEqual
	return data, password
	return JsonResponse(data)

class checkEmail(View):
	def post(self, request):
		data, userinfo={}, eval(request._body)
		#for item in request.POST.lists():
		#	if item: data, email={}, eval(item[0])
		email=userinfo['email']
		data['UserExisted']=True if User.objects.filter(email=email) else False
		return JsonResponse(data)

class passwordReset(View):
	def get(self, request): return render(request, 'password-reset.html') 
	def post(self, request):
		data, password=checkPasswordReset(request)
		me=request.user
		if data['passwordResetStatus']:
			me.set_password(password)
			#print('password reset')
			me.save()
		return JsonResponse(data)

class EditProfile(View):
	def get(self, request):return render(request, 'edit-profile.html') 
	def post(self, request, *args, **kwargs):
		data, rqstPst={}, request.POST
		first_name, last_name, nickname, email, cellular, birthday=rqstPst['first_name'], rqstPst['last_name'], rqstPst['nickname'], rqstPst['email'], rqstPst['cellular'], rqstPst['birthday']
		#user=checkUsername(username=email)
		user=request.user
		#user=User.objects.get_by_natural_key(username=identifier)
		#birthday.strftime('%Y-%m-%d')
		#user=request.user
		user.first_name, user.last_name, user.nickname=first_name, last_name, nickname
		user.email, user.cellular, user.birthday=email, cellular, birthday
		user.save()
		tmpl=loader.get_template('profile-template.html')
		data['ctx']=tmpl.render({'user':user}, request)
		data['profileUpdated']=True if user else False
		return JsonResponse(data)

class Logout(View):
	def post(self, request):
		rqstUser, rqstPst=request.user, request.POST
		auth_logout(request)
		return HttpResponseRedirect(reverse('index'))
		return super(LogoutView, self).get(request, *args, **kwargs)
		user = authenticate(identifier=identifier, password=password)
		if user and user.is_active:
			auth_login(request, user)
			return HttpResponseRedirect('home')
		else: return render(request, 'logout.html') 
	def get(self, request): return render(request, 'logout.html') 

class Invokers(View):
	def get(self, request):
		me=request.user
		invokers=Friend.objects.exclude(invoker=me)
		return render(request, 'invokers.html', dict(invokers=invokers))

class Others(View):
	def get(self, request):
		me=request.user
		others=User.objects.exclude(identifier=me)
		return render(request, 'others.html', dict(others=others))

class Login(View):
	def get(self, request): return render(request, 'login.html')
	def post(self, request):
		rqstPst=request.POST
		username, password=rqstPst['username'], rqstPst['password']
		me=checkUsername(username=username)
		#me=authenticate(request, username=username, password=password)
		#print(me, username, password)
		if me:
			if me.check_password(password):
				auth_login(request, me)
				return JsonResponse({'UserExisted':True})
			else: return JsonResponse({'ExistedWrongPassword':True})
		else: return JsonResponse({'UserExisted':False})
		#return HttpResponseRedirect(reverse('home'))
		#else: return JsonResponse({'UserExisted':False}) 
		'''
		try: user=User.objects.get_by_natural_key(username=username)
		except: assert 'DoesNotExist'
		user = authenticate(identifier=identifier, password=password)
		if me.is_authenticated: return HttpResponseRedirect(reverse('me'))
		'''

class Profile(View):
	def get(self, request, oid=None):
		other=User.objects.get(id=oid)
		postQueryset=other.author_post.filter(id__isnull=False)
		#author, author_id, body, id, media, post_blog, post_commentpost, post_commentsutra, post_forum, post_sutra, post_wallpost, timestamp
		wallQueryset=other.waller_wallpost.filter(post_id__isnull=False)
		#id, post, post_id, waller, waller_id
		print(postQueryset, wallQueryset)
		if not postQueryset.exists():
			if not wallQueryset.exists(): return render(request, 'profile.html', {'other':other})
			else: return render(request, 'profile.html', {'other':other, 'posts':wallQueryset.all()})
		latest_post, posts, idRange, count=qs.latest('timestamp'), tuple(), 5, 0
		pid=latest_post.id
		while not posts:
			pid, posts=fetchData(pid, idRange)
			idRange+=5
			if pid<2:break
		posts=(latest_post, )+posts
		print({'other':other, 'posts':posts})
		return render(request, 'profile.html', {'other':other, 'posts':posts, 'userID':request.user.id}) 
		posts=[post for post in other.author_post.all()]
		wallposts=[post for post in WallPost.objects.filter(waller=other)]
		posts+=wallposts
	'''
	def post(self, request, *args, **kwargs):
		userinfo=eval(request._body)
		identifier, first_name, last_name, password, email, cellular, birthday=userinfo['identifier'], userinfo['first_name'], userinfo['last_name'], userinfo['password'], userinfo['email'], userinfo['cellular'], userinfo['birthday']
		print(identifier, email, cellular)
	'''
class SignUp(View):
	def get(self, request): return render(request, 'signup.html') 
	def post(self, request, *args, **kwargs):
		userInfo=request.POST
		identifier, first_name, last_name, password, email, cellular, birthday=userInfo['identifier'], userInfo['first_name'], userInfo['last_name'], userInfo['password'], userInfo['email'], userInfo['cellular'], userInfo['birthday']
		UserExisted=checkUsername(username=identifier)
		EmailExisted=uniqueEmail(email=email)
		CellularExisted=uniqueCellular(cellular=cellular)
		if not UserExisted and not EmailExisted and not CellularExisted:
			me=User.objects.create_user(identifier, password, first_name=first_name, last_name=last_name, email=email, cellular=cellular, birthday=birthday)
			authenticate(request, username=identifier, password=password)
			if me and me.is_active:
				avatar=me.user_medium.create(is_avatar=True)
				auth_login(request, me)
			#me.set_password(password)
			#me.save()
			return JsonResponse({'UserCreated':True})
		else: return JsonResponse({'UserCreated':False})
'''
		user = authenticate(identifier=identifier, password=password)
		if user and user.is_active:
			auth_login(request, user)
			return HttpResponseRedirect('home')
		else: return render(request, 'signup.html') 
	def post(self, request):
		data={}
		identifier=request.post.get('identifier')
		user=User.objects.get_by_natural_key(username=identifier)
		data['UserExisted']=True if user else False
		return StreamingHttpResponse(data, content_type="application/json")

from django.utils.http import is_safe_url
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView

class LoginView(FormView):
    """ Provides the ability to login as a user with a username and password """
    success_url = '/auth/home/'
    template_name = 'login.html'
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        if self.request.session.test_cookie_worked(): self.request.session.delete_test_cookie()
        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        redirect_to = self.request.REQUEST.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to, host=self.request.get_host()): redirect_to = self.success_url
        return redirect_to
'''
