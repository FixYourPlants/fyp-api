# Register your models here.
from django.contrib import admin

from app.plants.models import Plant, Opinion, Characteristic, History


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    pass

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    pass


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    pass
