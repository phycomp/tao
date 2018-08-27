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
bo=Book.objects.get(id=4)
#chapter=Chapter.objects.get_or_create(id=1)
#Lines=open('/home/samuel/Downloads/道德.raw').readlines()
Lines=open('/home/samuel/Tao/經典/道德經/道德經全文.raw').readlines()
sec, chapterID=0, 0
me=User.objects.get(id=1)
for line in Lines:
	line=line.strip(' ').strip('\n')
	mat=search('(\w+)\s+(.*)', line)
	chapter, secBody=mat.group(1), mat.group(2)
	print(chapter, secBody)
	#if '凡' in line:continue
	'''
		chapter=line
		#chapterID+=1
		if not status:
			if co.chapter!=chapter:
				co.chapter=chapter
				co.save()
	else:
	'''
	co, status=Chapter.objects.get_or_create(chapter=chapter, book=bo)
	sec+=1
	#secBody=line
	print('sec=', sec, secBody, co, bo)
	#so, status=Section.objects.get_or_create(section=sec)
	sutra, status=Sutra.objects.get_or_create(section=sec, book=bo, chapter=co, author=me, body=secBody)
	#print(sutra)
	'''
	sutra.save()
	'''
