from django import forms
from django.contrib import admin
from django.utils.html import format_html

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'email_verified', 'googleAccount', 'image_preview')
    list_filter = ('email_verified', 'googleAccount', 'favourite_plant', 'affected_sicknesses')
    search_fields = ('username', 'email', 'about_me')
    ordering = ('username',)
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password', 'image', 'about_me')
        }),
        ('Permissions', {
            'fields': ('email_verified', 'googleAccount'),
            'classes': ('collapse',),
        }),
        ('Relationships', {
            'fields': ('favourite_plant', 'affected_sicknesses', 'history'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('image_preview',)
    filter_horizontal = ('favourite_plant', 'affected_sicknesses', 'history')
    list_per_page = 25

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 100px; height: 100px; object-fit: cover; border-radius: 50%;" />',
                obj.image.url
            )
        return "(No image)"
    image_preview.short_description = "Image Preview"

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['password'].widget = forms.PasswordInput()
        return form

