from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.sessions.models import Session
from .models import Image


@receiver(post_save, sender=Session)
def reset_points_on_session_start(sender, instance, created, **kwargs):
    if created:
        # Сброс счетчика points у всех объектов Image до 0
        Image.objects.all().update(points=0)
