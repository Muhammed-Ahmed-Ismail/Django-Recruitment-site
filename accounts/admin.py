from django.contrib import admin

# Register your models here.
from .models import User, Developer, Company


class UserAdmin(admin.ModelAdmin):
    pass


class DeveloperAdmin(admin.ModelAdmin):
    pass


class CompanyAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Developer, DeveloperAdmin)
