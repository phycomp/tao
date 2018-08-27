from django.db.models.signals import post_save
from notifications.signals import notify
from .models import Member

def member_notif(sender, instance, created, **kwargs):
    notify.send(instance, verb='was saved')

post_save.connect(member_notif, sender=Member)
