from django.contrib import admin

from .models import AlluploadsImage, AlluploadsFile


class AlluploadsImageAdmin(admin.ModelAdmin):
    list_display = ["id", "content_type", "object_id", "image", "is_selected"]

    class Meta: 
        model = AlluploadsImage


class AlluploadsFileAdmin(admin.ModelAdmin):
    list_display = ["id", "content_type", "object_id", "file", "is_selected"]

    class Meta: 
        model = AlluploadsFile


admin.site.register(AlluploadsImage, AlluploadsImageAdmin)
admin.site.register(AlluploadsFile, AlluploadsFileAdmin)