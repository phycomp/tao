from django.db.models import ForeignKey, Model, CASCADE, SlugField, CharField, BooleanField, ManyToManyField, TextField, DateTimeField
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import site, ModelAdmin
#from django.contrib.contenttypes.fields import GenericRelation
from book.models import Book, Chapter	#, Section
from post.models import Post
AUTH_USER_MODEL=settings.AUTH_USER_MODEL

class Sutra(Model):
	book=ForeignKey(Book, related_name='book_sutra', on_delete=CASCADE)
	chapter=ForeignKey(Chapter, related_name='chapter_sutra', on_delete=CASCADE)
	section=CharField(_('Section'), max_length=3)
	post=ForeignKey(Post, related_name='post_sutra', on_delete=CASCADE)
	timestamp=DateTimeField(_('timestamp'), auto_now=True)
	#section=ForeignKey(Section, related_name='section_sutra', on_delete=CASCADE)
	#slug=SlugField(_('Slug'), max_length=90, unique=settings.PINAX_BLOG_SLUG_UNIQUE)
	def __str__(self): return ' '.join([self.book.book, self.chapter.chapter, self.section])
	'''
	def __str__(self): return self.book.book
	@property
	def get_book(self):return self.book.book
	@property
	def get_chapter(self):return self.chapter.chapter
	@property
	def get_section(self):return str(self.section)
	'''
	class Meta: db_table='sutra'

class CommentSutra(Model):
	sutra=ForeignKey(Sutra, related_name='sutra_commentsutra', on_delete=CASCADE)
	commentsutra=ForeignKey('self', related_name='commentsutra_commentsutra', on_delete=CASCADE, null=True)
	commentor=ForeignKey(AUTH_USER_MODEL, verbose_name=_('Commentor'), related_name='commentor_sutra', on_delete=CASCADE)
	#post=ForeignKey(Post, related_name='post_commentsutra', on_delete=CASCADE)
	body=TextField()
	timestamp=DateTimeField(_('timestamp'), auto_now=True)
	def __str__(self): return self.body[:10]
	class Meta: db_table='comment_sutra'
	'''
	body=TextField()
	@property
	def comments(self): return self.sutra.sutra_commentsutra.filter(commentsutra__isnull=True)
	'''
'''
class CommentSutra(Post):
	comment=ManyToManyField(Sutra, related_name='comment_sutra')
	#def __str__(self): return self.comment	#.body[:10]
	class Meta: db_table='comment_sutra'
	#comment=ForeignKey(Sutra, related_name='sutra_comment', on_delete=CASCADE)
	#commentor=ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Commentor'), related_name='commentor_on_sutra', on_delete=CASCADE)
	#created=DateTimeField(_('Created'), auto_now=True)
	#image=ManyToManyField(Image, related_name='image_sutra', on_delete=CASCADE)
	#updated=DateTimeField(_('Updated'), null=True, blank=True, editable=False)
	#published=DateTimeField(_('Published'), null=True, blank=True)  # when last published state=models.IntegerField(_('State'), choices=STATE_CHOICES, default=STATE_CHOICES[0][0])
	#secret_key=CharField( _('Secret key'), max_length=8, blank=True, unique=True, help_text=_('allows url for sharing unpublished posts to unauthenticated users'))
	#view_count=IntegerField(_('View count'), default=0, editable=False)
'''
