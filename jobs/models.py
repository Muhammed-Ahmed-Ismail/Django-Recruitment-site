from django.db import models

# Create your models here.


# Job Model :
# Fields:
# ●name
# ●creation_time
# ●Modification_time
# ●Description
# ●Tags (Many2Many with tag model)
# ●applied_developers (Many2Many with user model who has applied for it)
# ●developer (Accepted developer by job owner)
# ●created_by (owner “user of type recruiter”)
# ●status (‘open’,’inprogress’,’finished’)

# Actions:
# -On Create Send notification to all developers who have tags matched
# -On developer accept Notify accepted developer with acceptance & all other developers  with rejection
# -On Job finish send notification to job owner
from accounts.models import Company


class Job(models.Model):
    class Status(models.TextChoices):
        OPEN = 'O', 'open'
        INPROGRESS = 'IN', 'inprogress'
        FINISHED = 'F', 'finished'

    name = models.CharField(max_length=30)
    creation_time = models.DateTimeField(auto_now_add=True)
    Modification_time = models.DateTimeField(auto_now=True)
    Description = models.TextField(max_length=255)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.OPEN,
    )

    # Tags= models.CharField(max_length=30)
    # many to many with tags model

    # applied_developers = models.CharField(max_length=30)
    # Many2Many with user model who has applied for it

    # developer = models.CharField(max_length=30)
    # created_by = models.CharField(max_length=30)

    image = models.CharField(max_length=255, default='https://dummyimage.com/200x300/000/ffffff')
    created_by = models.ForeignKey(Company, on_delete=models.CASCADE)
    applied_developer = models.ManyToManyField('accounts.developer', blank=True)
    tags = models.ManyToManyField('tags.tag')

    def add_new_application(self, developer):
        self.applied_developer.add(developer)
        self.save()

    def assign_to_developer(self, developer):
        print('from assign',developer)
        refused_developers = list(filter(lambda d: d.id != developer.id, self.applied_developer.all()))
        developer.get_accepted()
        for developer in refused_developers:
            developer.get_rejected()
        pass
