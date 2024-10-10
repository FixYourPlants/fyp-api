# Register your models here.
from django.contrib import admin
from django.utils.html import format_html

from app.sickness.models import Sickness


@admin.register(Sickness)
class SicknessAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'image_preview')
    list_filter = ('notifications',)
    search_fields = ('name', 'description', 'treatment')
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'treatment', 'image', 'notifications')
        }),
    )
    readonly_fields = ('image_preview',)
    filter_horizontal = ('notifications',)
    list_per_page = 25

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 100px; height: 100px; object-fit: cover; border-radius: 50%;" />',
                obj.image.url
            )
        return "(No image)"
    image_preview.short_description = "Image Preview"

    def short_description(self, obj):
        return obj.description[:75] + ('...' if len(obj.description) > 75 else '')
    short_description.short_description = 'Description'
