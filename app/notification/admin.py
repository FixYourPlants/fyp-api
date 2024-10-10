# Register your models here.

from django.contrib import admin

from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'short_description')
    list_filter = ('timestamp',)
    search_fields = ('title', 'description')
    ordering = ('-timestamp',)
    date_hierarchy = 'timestamp'
    fieldsets = (
        (None, {
            'fields': ('title', 'description')
        }),
        ('Dates', {
            'fields': ('timestamp',),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('timestamp',)
    list_per_page = 25

    def short_description(self, obj):
        return obj.description[:75] + ('...' if len(obj.description) > 75 else '')
    short_description.short_description = 'Description'

