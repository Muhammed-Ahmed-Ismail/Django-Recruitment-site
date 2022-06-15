from django.db import models

# Actions:
# -On Create Send notification to all developers who have tags matched
# -On developer accept Notify accepted developer with acceptance & all other developers  with rejection
# -On Job finish send notification to job owner
from accounts.models import Company


class Job(models.Model):
    name = models.CharField(max_length=30)
    creation_time = models.DateTimeField(auto_now_add=True)
    Modification_time = models.DateTimeField(auto_now=True)
    Description = models.TextField(max_length=255)

    # Tags= models.ManyToManyField('tags.tag')
    
    # applied_developers = models.CharField(max_length=30)
        #Many2Many with user model who has applied for it
    # developer = models.CharField(max_length=30)
    # created_by = models.CharField(max_length=30)

    image = models.CharField(max_length=255, default='https://dummyimage.com/200x300/000/ffffff')
    created_by = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Status(models.TextChoices):
        OPEN = 'O', 'open'
        INPROGRESS = 'IN', 'inprogress'
        FINISHED = 'F', 'finished'

    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.OPEN,
    )
