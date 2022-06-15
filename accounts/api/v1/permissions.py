from rest_framework.permissions import BasePermission


###
#  **** convention *****
#   company permissions start with Comp
#   developer permissions start with Dev
#   ends with Permission
#   between is description
###

###
# company permissions
#   as a company I want to see my posted jobs In the wall page
#   as a company, I want to edIt a job I posted or delete It as It Is not opened yet
#   as a company, I want to mark a job to be done
#   as a company I want to choose a developer and send him/her an acceptance email
#   as a company I want to send a rejectIon emaIl for other developers that I dId not select
###

# company and developer permission
from jobs.models import Job


# Both company and developer can see listed jobs
class CompDevJobsPermission(BasePermission):
    def has_permission(self, request, view):
        if (
                request.user.user_type == 'DEVELOPER' or
                request.user.user_type == 'COMPANY'
        ):
            return True
        return False


# only companies create jobs
class CompCreateJobPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_type == 'COMPANY':
            return True
        return False


# get this company jobs (doesn't make sense, but it is a requirement)
class CompGetMyJobsPermission(BasePermission):
    def has_permission(self, request, view):
        job_id = view.kwargs.get('job_id')
        job = Job.objects.filter(id=job_id).first()
        if (
                request.user.user_type == 'DEVELOPER'
                and request.user.id == job.created_by.user.id
        ):
            return True
        return False


# edit, delete, mark done
class CompEditMyJopPermission(BasePermission):
    def has_permission(self, request, view):
        job_id = view.kwargs.get('job_id')
        job = Job.objects.filter(id=job_id).first()
        if (
                request.user and
                request.user.user_type == 'COMPANY' and
                request.user.id == job.created_by.user.id
        ):
            return True
        return False


###
# developer permissions
# as a developer I want to see the available jobs in the wall page ^ CompDevJobsPermission
# as a developer I want to choose a job to apply for
# as a developer, I want to mark job done
###

class DevApplyForJobPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_type == 'DEVELOPER':
            return True
        return False


class DevMarkJobDonePermission(BasePermission):
    def has_permission(self, request, view):
        job_id = view.kwargs.get('job_id')
        job = Job.objects.filter(id=job_id)
        if (
                request.user.user_type == 'DEVELOPER'
                # and
                # request.user.username == job.
        ):
            return True
        return False
