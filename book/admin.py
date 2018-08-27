from django.contrib.admin import site, ModelAdmin

from .models import Chapter, Book

'''
class SectionAdmin(ModelAdmin):
	model=Section
site.register(Section, SectionAdmin)
'''

class ChapterAdmin(ModelAdmin):
	model=Chapter
site.register(Chapter, ChapterAdmin)

class BookAdmin(ModelAdmin):
	model=Book
site.register(Book, BookAdmin)
