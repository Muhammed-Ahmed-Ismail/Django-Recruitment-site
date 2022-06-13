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
class Job(models.Model):

    name = models.CharField(max_length=30)
    creation_time = models.DateTimeField(auto_now_add=True)
    Modification_time = models.DateTimeField(auto_now=True)
    Description = models.TextField(max_length=255)
    tags = models.ManyToManyField('tags.tag')

    # many to many with tags model

    # applied_developers = models.CharField(max_length=30)
    #Many2Many with user model who has applied for it

    # developer = models.CharField(max_length=30)
    # created_by = models.CharField(max_length=30)
    class status(models.TextChoices):
        OPEN = 'O', ('open')
        INPROGRESS = 'IN', ('inprogress')
        FINISHED = 'F', ('finished')

    status = models.CharField(
        max_length=2,
        choices=status.choices,
        default=status.OPEN,
    )