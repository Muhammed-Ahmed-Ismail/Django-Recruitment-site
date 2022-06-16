from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Job
@receiver(post_save,sender=Job)
def todo_post_save_action(*args, **kwargs):
    if kwargs.get('created'):
        job = kwargs.get('instance')
        tags = job.tags
        developers_to_notify = {}
        for tag in tags:
            developers_to_notify.add(set(tag.developer.all()))

        print(developers_to_notify)
