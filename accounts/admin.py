from django.contrib import admin
from .models import User, Developer, Company



class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'user_type', 'gender', 'date_of_birth']


class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['user', 'job', 'cv', 'tags', 'can_apply', 'notify_by_mail']


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['user', 'history', 'address']


admin.site.register(User)
admin.site.register(Company)
admin.site.register(Developer)
