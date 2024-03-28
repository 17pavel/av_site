from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Jobs
from scheduled_tasks import schedule_jobs


@receiver(post_save, sender=Jobs)
def run_jobs(sender, instance, created, **kwargs):
    if created:
        schedule_jobs(instance)
