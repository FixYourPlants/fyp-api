# Register your models here.
from django.contrib import admin
from django.utils.html import format_html

from app.plants.models import Plant, Opinion, Characteristic, History


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'scientific_name', 'difficulty', 'image_preview')
    list_filter = ('difficulty', 'sicknesses', 'characteristics')
    search_fields = ('name', 'scientific_name', 'description')
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'scientific_name', 'description', 'image')
        }),
        ('Advanced options', {
            'fields': ('difficulty', 'treatment', 'sicknesses', 'characteristics', 'notifications'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('image_preview',)
    filter_horizontal = ('sicknesses', 'characteristics', 'notifications')
    list_per_page = 25

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('sicknesses', 'characteristics', 'notifications')

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 100px; height: 100px; object-fit: cover; border-radius: 50%;" />',
                obj.image.url
            )
        return "(No image)"

    image_preview.short_description = "Image Preview"


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'plant', 'sickness', 'image_preview')
    list_filter = ('created_at', 'plant', 'sickness')
    search_fields = ('plant__name', 'sickness__name')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    fieldsets = (
        (None, {
            'fields': ('plant', 'sickness', 'image')
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
        return qs.select_related('plant', 'sickness')

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 100px; height: 100px; object-fit: cover; border-radius: 50%;" />',
                obj.image.url
            )
        return "(No image)"

    image_preview.short_description = "Image Preview"


@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    list_display = ('title', 'plant', 'user', 'created_at', 'short_description')
    list_filter = ('created_at', 'plant', 'user')
    search_fields = ('title', 'plant__name', 'user__username', 'description')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'plant', 'user')
        }),
        ('Dates', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at',)
    list_per_page = 25

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('plant', 'user')

    def short_description(self, obj):
        return obj.description[:75] + ('...' if len(obj.description) > 75 else '')
    short_description.short_description = 'Description'


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name',)
    ordering = ('name',)
    fields = ('name',)
    list_per_page = 25
