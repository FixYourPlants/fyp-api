from django.contrib import admin

from app.notification.models import Notification


# Register your models here.
from django.contrib import admin
from .models import Notification

from django.contrib import admin
from .models import Notification

from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('title', 'description')
    fields = ('title', 'timestamp', 'description')


