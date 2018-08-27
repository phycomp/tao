# -*- encoding: utf-8
from uuid import uuid4
from django.db.models import Model, UUIDField, FileField, TextField, CharField, DateTimeField, ForeignKey, CASCADE
from django.conf import settings
from django.contrib.auth.models import User

class SoundFile(Model):
    TYPE_CHOICES = (
        ('wav', 'wav'),
    )
    uuid = UUIDField(primary_key=True, default=uuid4)
    file = FileField(upload_to=settings.OUTPUT_DIR)
    text = TextField(blank=False)
    command = CharField(max_length=255, blank=True)
    type = CharField(max_length=5, choices=TYPE_CHOICES)
    dc = DateTimeField(auto_now_add=True)
    user = ForeignKey(User, blank=True, null=True, on_delete=CASCADE)

    def __str__(self): return '%s' % self.uuid
