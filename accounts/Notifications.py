# from re import template
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.template.loader import render_to_string


def send_mail_to_devs_w_matching_tags(self, tags):
    template = render_to_string('./templates/email_template.html')
    email = EmailMessage(
        'Jobs you might be intreseted in',  # subject
        template,  # body
        settings.EMAIL_HOST_USER,  # sender mail
        ['adham.ahm.hassan@gmail.com'],  # All developers with matching tags to the created job
    )
    email.fail_silently = True
    email.send()


def send_acceptance_mail(reciever):
    print('form sendemail')
    # template = render_to_string('accounts/templates/acceptance_mail.html')
    # print(template)
    # email = EmailMessage(
    #     'Congratulations! You have been accepted',  # subject
    #     '''Congratulations !
    #     You have been selected to do the job
    #     Best Regards
    #     Team ITI''',  # body
    #     settings.EMAIL_HOST_USER,  # sender mail
    #     reciever,  # reciever mail (Accepted developer's email)
    # )
    # print(email)
    # email.fail_silently = False
    # email.send()
    subject = 'Congratulations! You have been accepted'
    msg = '''Congratulations !
        You have been selected to do the job 
        Best Regards
        Team ITI'''
    receivers = [reciever]
    send_mail(subject=subject, message=msg, from_email='notifiersys@gmail.com', recipient_list=receivers)


def send_rejection_mail(reciever):
    # template = render_to_string('./templates/rejection_mail.html')
    # email = EmailMessage(
    #     'Better luck next time !',  # subject
    #     template,  # body
    #     settings.EMAIL_HOST_USER,  # sender mail
    #     reciever,  # reciever mail ( list of rejected developer's emails)
    # )
    # email.fail_silently = True
    # email.send()
    subject = 'Better luck next time !'
    msg = '''Hello,
            We are sorry to tell you that you have not been selected to do the job 
            Best Regards
            Team ITI'''
    receivers = [reciever]
    send_mail(subject=subject, message=msg, from_email='notifiersys@gmail.com', recipient_list=receivers)


def send_job_finished_mail(reciever):
    template = render_to_string('./templates/job_finished.html')
    email = EmailMessage(
        'Job finished !',  # subject
        template,  # body
        settings.EMAIL_HOST_USER,  # sender mail
        reciever,  # reciever mail (Recruiter whose job has been finished)
    )
    email.fail_silently = True
    email.send()
