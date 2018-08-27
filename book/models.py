from django.db.models import Model, ForeignKey, DateTimeField, TextField, CASCADE, CharField
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
AUTH_USER_MODEL=settings.AUTH_USER_MODEL

class Book(Model):
	author=ForeignKey(AUTH_USER_MODEL, verbose_name=_('Author'), related_name='author_book', on_delete=CASCADE)
	book=CharField(_('Book'), max_length=10, unique=True)
	timestamp=DateTimeField(_('timestamp'), auto_now=True)
	def __str__(self): return self.book
	@property
	def bookAuthorID(self): return self.author_id
	class Meta: db_table='book'

class Chapter(Model):
	book=ForeignKey(Book, related_name='book_chapter', on_delete=CASCADE, null=False)
	chapter=CharField(_('Chapter'), max_length=10)	#, unique=True)
	timestamp=DateTimeField(_('timestamp'), auto_now=True)
	def __str__(self): return self.chapter
	#def __str__(self): return ' '.join([self.book.book, self.chapter])
	class Meta:
		db_table='chapter'
		get_latest_by='timestamp'

'''
class Section(Model):
	#book=ForeignKey(Book, related_name='book_section', on_delete=CASCADE)
	#chapter=ForeignKey(Chapter, related_name='chapter_section', on_delete=CASCADE)
	section=CharField(_('Section'), max_length=10, unique=True)
	created=DateTimeField(_('Created'), auto_now=True)
	def __str__(self): return self.section
	class Meta: db_table='section'
'''
