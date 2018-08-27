#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django.http import HttpResponseRedirect
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from re import compile
from django.urls import reverse

LOGIN_URL, MEDIA_URL=settings.LOGIN_URL, settings.MEDIA_URL
LOGIN_EXEMPT_URLS=[ LOGIN_URL, MEDIA_URL, '/admin/', reverse('access'),
	reverse('signup'), reverse('password-forgot'),
	reverse('about'), reverse('contact'), reverse('leaflet'), reverse('index'), 
	 #r'^member/signup/', r'^member/password-forgot/', r'^about/', r'^contact/', r'^$',
]
INDEX=compile(reverse('index').lstrip('/'))
editDelete=[compile(url) for url in ['edit', 'delete']]
#EXEMPT_URLS=(LOGIN_URL, )+LOGIN_EXEMPT_URLS
#EXEMPT_URLS = [compile(LOGIN_URL.lstrip('/'))]
EXEMPT_URLS = [compile(url.lstrip('/')) for url in LOGIN_EXEMPT_URLS]
class LoginRequiredMiddleware(MiddlewareMixin):
	def process_request(self, request):
		me=request.user
		if not me.is_authenticated:
			path = request.path_info.lstrip('/')
			if not path: pass#return HttpResponseRedirect(reverse('index'))
			elif not any(m.match(path) for m in EXEMPT_URLS if m!=INDEX):
				return HttpResponseRedirect(LOGIN_URL)
		#elif not any(m.match(path) for m in editDelete):
		#if me==request.hasattr('blog')
		#elif not any(m.match(path) for m in filter(lambda url:url!=INDEX, EXEMPT_URLS)):
		#if hasattr(request, 'post'): print(request.post.author==request.user)

from django.template.response import SimpleTemplateResponse
from django.conf import settings
#from django.http import HttpResponse
#from django.shortcuts import render
AUTHOR_APPS=settings.AUTHOR_APPS+['ge', ]

class PostAuthMiddleWare(MiddlewareMixin):
	def __init__(self, get_response):
		self.get_response = get_response
	def __call__(self, request):
		response = self.get_response(request)
		#print(hasattr(response, 'post'))
		return response
	def process_template_response(self, request, response):
		me, context_data=request.user, response.context_data
		#author, me=context_data['forum'].post.author, request.user
		Authors=[]
		for author_app in AUTHOR_APPS:
			app=context_data.get(author_app) 
			if app: Authors.append(app)
		#authors=[author for author in Authors if author]
		if Authors:
			for Author in Authors:
				if hasattr(Author, 'post'): author=Author.post.author
				elif hasattr(Author, 'tug'): author=Author.media.last().user.last()
				elif hasattr(Author, 'galler'): author=Author.galler
				elif hasattr(Author, 'gallery'): author=Author.gallery.galler
				else: author=Author.author
			if author!=me: return SimpleTemplateResponse('permission-not-granted.html')	#HttpResponse()
		else: return response
		if hasattr(context_data, 'forum'):
			print(context_data.forum.post.author==request.user)
			print('response', response)
