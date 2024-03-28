from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete, pre_save
from .models import Message
from scheduled_tasks import sent_answer


@receiver(post_save, sender=Message)
def answer(sender, instance, **kwargs):
        sent_answer(instance)
