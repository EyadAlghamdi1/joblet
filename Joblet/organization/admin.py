from django.contrib import admin
from .models import Organization
# Register your models here.

class orgAdmin(admin.ModelAdmin):
    list_display = ['name', 'approved']
admin.site.register(Organization, orgAdmin)


