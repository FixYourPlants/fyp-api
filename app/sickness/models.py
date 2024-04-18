from enum import Enum

from django.db import models


# Create your models here.
class Treatment(models.Model):
    # Atributos
    actions = models.TextField()
    type = models.IntegerField()

    # Relaciones
    sickness = models.ForeignKey('Sickness', on_delete=models.CASCADE)
    plant = models.ForeignKey('plants.Plant', on_delete=models.CASCADE, related_name='treatment_instances')

    def __str__(self):
        return self.actions


class Sickness(models.Model):
    # Atributos
    name = models.CharField(max_length=100)
    description = models.TextField()

    # Relaciones
    plants = models.ManyToManyField('plants.Plant', related_name="plant_sicknesses")
    treatments = models.ForeignKey(Treatment, on_delete=models.CASCADE, related_name="treatment_sicknesses")

    def __str__(self):
        return self.name

class TypeTreatment(Enum):
    PLANTS = 1
    SICKNESS = 2
