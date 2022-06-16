from django.contrib import admin
from .models import Job, Company

class JobAdmin(admin.ModelAdmin):
    list_display = ['name', 'creation_time', 'Modification_time', 'Description', 'created_by', 'status']
    search_fields = ['created_by__user__username','applied_developer__user__username']
    list_filter = ['name', 'status']

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return False
        return True
        
    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(Job, JobAdmin)

