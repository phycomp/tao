#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.conf import settings
from os import environ
environ['DJANGO_SETTINGS_MODULE']='tao.settings'
from django.contrib.auth import get_user_model
from book.models import Book, Chapter	#, Section
from sutra.models import Sutra
from re import search, match, findall
from sys import argv

User=get_user_model()
bo=Book.objects.get(id=6)
#chapter=Chapter.objects.get_or_create(id=1)
#Lines=open('/home/samuel/Downloads/道德.raw').readlines()
Lines=open('/home/samuel/弟子規').readlines()
me=User.objects.get(id=1)
for line in Lines:
	line=line.strip(' ').strip('\n')
	if '#' in line:continue
	elif line[0] in ['第', '總']:
		sec=0
		#mat=search('(\w+)\s+(.*)', line)
		chapter=line
		print(chapter)
		co, status=Chapter.objects.get_or_create(chapter=chapter, book=bo)
	else:
		secBody=line
		#print(chapter, secBody)
		sec+=1
		sutra, status=Sutra.objects.get_or_create(section=sec, book=bo, chapter=co, author=me, body=secBody)
		print('info=', sec, secBody, chapter, bo.id)
	'''
		chapter=line
		#chapterID+=1
		if not status:
			if co.chapter!=chapter:
				co.chapter=chapter
				co.save()
	else:
	'''
	#secBody=line
	#so, status=Section.objects.get_or_create(section=sec)
	#print(sutra)
	'''
	sutra.save()
	'''
