# coding: utf-8
from rest_framework.serializers import ValidationError, UUIDField, Serializer, CharField
from .models import SoundFile


class Generation(Serializer):
    text = CharField(required=True)


class GetFile(Serializer):
    uuid = UUIDField(required=True)

    def validate_uuid(self, value):
        if not SoundFile.objects.filter(uuid=value).exists():
            raise ValidationError('Sound file with uuid "%s" not found' % value)
        return value
