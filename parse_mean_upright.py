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
bo, status=me.author_book.get_or_create(book=u'中庸證釋')
Lines=open('/home/samuel/Downloads/中庸證釋.raw').readlines()
sec, chapterID=0, 0
for idx, line in enumerate(Lines):
	line=line.strip(' ').strip('\n')
	#if '凡' in line:continue
	if line.startswith('第'):
		chapter=line
		print(chapter)
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
		#so, status=Section.objects.get_or_create(section=sec)
		post=me.author_post.create(body=secBody)
		sutra, status=post.post_sutra.get_or_create(section=sec, book=bo, chapter=co)
		#print(sutra)
		'''
		sutra.save()
		'''
