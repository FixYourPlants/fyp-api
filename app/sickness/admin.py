# Register your models here.
from django.contrib import admin

from app.sickness.models import Sickness

@admin.register(Sickness)
class SicknessAdmin(admin.ModelAdmin):
    pass
