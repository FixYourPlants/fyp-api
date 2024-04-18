# Register your models here.
from django.contrib import admin

from app.sickness.models import Treatment, Sickness


@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    pass

@admin.register(Sickness)
class SicknessAdmin(admin.ModelAdmin):
    pass
