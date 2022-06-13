from django.contrib import admin

# Register your models here.
from .models import Tag
class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tag, TagAdmin)