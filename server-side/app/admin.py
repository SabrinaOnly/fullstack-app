from django.contrib import admin, auth

from .models import Record

admin.site.unregister(auth.models.Group)

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['name', 'tel']
