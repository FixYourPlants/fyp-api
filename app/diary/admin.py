# Register your models here.
from django.contrib import admin
from django.utils.html import format_html

from app.diary.models import Page
from .models import Diary


@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'plant', 'user', 'updated_at')
    list_filter = ('updated_at', 'plant', 'user')
    search_fields = ('title', 'plant__name', 'user__username')
    ordering = ('-updated_at',)
    date_hierarchy = 'updated_at'
    fieldsets = (
        (None, {
            'fields': ('title', 'plant', 'user')
        }),
        ('Dates', {
            'fields': ('updated_at',),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('updated_at',)
    list_per_page = 25

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('plant', 'user')



@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'diary', 'created_at', 'image_preview')
    list_filter = ('created_at', 'diary')
    search_fields = ('title', 'diary__title')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'diary', 'image')
        }),
        ('Dates', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'image_preview')
    list_per_page = 25

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('diary')

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 100px; height: 100px; object-fit: cover; border-radius: 50%;" />',
                obj.image.url
            )
        return "(No image)"
    image_preview.short_description = "Image Preview"
