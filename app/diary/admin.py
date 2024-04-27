# Register your models here.
from django.contrib import admin

from app.diary.models import Diary, Page


@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    pass


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass
