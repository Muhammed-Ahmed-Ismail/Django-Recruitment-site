from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed
from .models import Job
from notifications.models import Notification


# @receiver(post_save,sender=Job)
# def todo_post_save_action(*args, **kwargs):
#     if kwargs.get('created'):
#         job = kwargs.get('instance')
#         print(job)
#         tags = job.name
#         print(tags)
#         # developers_to_notify = {}
#         # for tag in tags:
#         #     developers_to_notify.add(set(tag.developer.all()))
#         #
#         # print(developers_to_notify)
@receiver(m2m_changed, sender=Job.tags.through)
def jop_post_save_action(sender, instance, action, **kwargs):
    print('ASASA',Notification.objects.all())

    # notification = Notification.objects.create(name="New Job", message="sdasdas")
    if action == 'post_add':
        tags = instance.tags.all()
        developers_to_notify = []
        notification = Notification.objects.create(name="Job is created",message=f'{instance.name} is created')

        # print(notification)
        for tag in tags:
            developers_to_notify.extend(list(tag.developer_set.all()))

        developers_to_notify = set(developers_to_notify)
        print(developers_to_notify)
        for developer in developers_to_notify:
            print(type(developer))
            developer.notify(notification)
            print(developer)

