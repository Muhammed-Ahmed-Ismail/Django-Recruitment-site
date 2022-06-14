# from re import template
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


class Notifications():
    def send_mail_to_devs_w_matching_tags(self,tags):
        template = render_to_string('./templates/email_template.html')
        email = EmailMessage(
        'Jobs you might be intreseted in',#subject
        template,#body
        settings.EMAIL_HOST_USER,#sender mail
        ['adham.ahm.hassan@gmail.com'],# All developers with matching tags to the created job
        )
        email.fail_silently = True
        email.send()

    def send_acceptance_mail(self):
        template = render_to_string('./templates/acceptance_mail.html')
        email = EmailMessage(
        'Congratulations! You have been accepted',#subject
        template,#body
        settings.EMAIL_HOST_USER,#sender mail
        ['adham.ahm.hassan@gmail.com'],#reciever mail (Accepted developer's email)
        )
        email.fail_silently = True
        email.send()

    def send_rejection_mail(self):
        template = render_to_string('./templates/rejection_mail.html')
        email = EmailMessage(
        'Better luck next time !',#subject
        template,#body
        settings.EMAIL_HOST_USER,#sender mail
        ['adham.ahm.hassan@gmail.com'],#reciever mail ( list of rejected developer's emails)
        )
        email.fail_silently = True
        email.send()


    def send_job_finished_mail(self):
        template = render_to_string('./templates/job_finished.html')
        email = EmailMessage(
        'Job finished !',#subject
        template,#body
        settings.EMAIL_HOST_USER,#sender mail
        ['adham.ahm.hassan@gmail.com'],#reciever mail (Recruiter whose job has been finished)
        )
        email.fail_silently = True
        email.send()
            