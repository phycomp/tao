from haystack.indexes import SearchIndex, Indexable, CharField, DateTimeField, EdgeNgramField
from .models import Blog
from django.utils.timezone import now
from pytz import UTC
now=now()
#from datetime import datetime
#kwargs==>model_attr=None, use_template=False, template_name=None, document=False, indexed=True, stored=True, faceted=False, default=NOT_PROVIDED, null=False, index_fieldname=None, facet_class=None, boost=1.0, weight=None
#datetime.now()	#datetime(2013, 11, 20, 20, 8, 7, 127325, tzinfo=UTC)

class BlogIndex(SearchIndex, Indexable):
	text=CharField(document=True, use_template=True)
	author=CharField(model_attr='author', faceted=True)
	title=CharField(model_attr='title', use_template=True)	#, indexed=False)
	body=EdgeNgramField(model_attr='body', use_template=True)
	timestamp=DateTimeField(model_attr='created')
	def get_model(self): return Blog
	def index_queryset(self, using=None): return self.get_model().objects.filter(created__lte=now)
	def prepare_body(self, obj): return obj.body
	def prepare_text(self, obj): return obj.text
