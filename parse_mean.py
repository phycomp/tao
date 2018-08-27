#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.conf import settings
from os import environ
environ['DJANGO_SETTINGS_MODULE']='tao.settings'
from django.contrib.auth import get_user_model
from book.models import Book, Chapter	#, Section
from sutra.models import Sutra
from re import match, findall
from sys import argv

User=get_user_model()
me=User.objects.get(id=1)
bo, status=me.author_book.get_or_create(book=u'中庸')
#bo=Book.objects.get(id=2)
#chapter=Chapter.objects.get_or_create(id=1)
Lines=open('/home/samuel/Tao/通識道義/中庸全文.raw').readlines()
sec, chapterID=0, 0
for idx, line in enumerate(Lines):
	line=line.strip(' ').strip('\n')
	#if '凡' in line:continue
	if line.startswith('第'):
		chapter=line
		#chapterID+=1
		co, status=Chapter.objects.get_or_create(chapter=chapter, book=bo)
		'''
		if not status:
			if co.chapter!=chapter:
				co.chapter=chapter
				co.save()
		'''
	else:
		sec+=1
		secBody=line
		print('sec=', sec, secBody, co, bo)
		post=me.author_post.create(body=secBody)
		sutra, status=post.post_sutra.get_or_create(section=sec, book=bo, chapter=co)
		'''
		#so, status=Section.objects.get_or_create(section=sec)
		sutra, status=Sutra.objects.get_or_create(section=sec, book=bo, chapter=co, author=me, body=secBody)
		#print(sutra)
		sutra.save()
		'''
