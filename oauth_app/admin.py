from django.contrib import admin
from .models import MyFile
from django.utils.html import format_html
from django.utils.safestring import mark_safe

@admin.register(MyFile)
class MyFileAdmin(admin.ModelAdmin):
    list_display = ['title', 'description','file', 'uploaded_at', 'file_link']  # Include 'file_link' in list_display
    readonly_fields = ['uploaded_at']

    def file_link(self, obj):
        if obj.file:
            return mark_safe("<a href='{url}'>{url}</a>".format(url=obj.file.url))
        return "No attachment"

    file_link.short_description = 'File URL'