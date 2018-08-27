from haystack.indexes import SearchIndex, Indexable, CharField, DateTimeField, EdgeNgramField
from .models import Member
from django.utils.timezone import now
from pytz import UTC
now=now()
#from datetime import datetime
#kwargs==>model_attr=None, use_template=False, template_name=None, document=False, indexed=True, stored=True, faceted=False, default=NOT_PROVIDED, null=False, index_fieldname=None, facet_class=None, boost=1.0, weight=None
#datetime.now()	#datetime(2013, 11, 20, 20, 8, 7, 127325, tzinfo=UTC)

class MemberIndex(SearchIndex, Indexable):
	text=CharField(document=True, use_template=True)
	identifier=CharField(model_attr='identifier')
	email=CharField(model_attr='email', use_template=True)
	cellular=EdgeNgramField(model_attr='cellular', use_template=True)
	#rendered=CharField(use_template=True, indexed=False)
	timestamp=DateTimeField(model_attr='created')
	def get_model(self): return Member
	def index_queryset(self, using=None): return self.get_model().objects.filter(created__lte=now)
	def prepare_cellular(self, obj): return obj.cellular
