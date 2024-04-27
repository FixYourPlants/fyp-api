from enum import Enum

import uuid
from django.db import models

from app.sickness.models import Sickness
from app.users.models import User


# Create your models here.
class Difficulty(Enum):
    EASY = 'FÁCIL'
    MEDIUM = 'MEDIO'
    HIGH = 'ALTA'



class Plant(models.Model):
    # Atributos
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="plants/", null=True, blank=True)
    difficulty = models.CharField(choices=[(tag.name, tag.value) for tag in Difficulty], max_length=10,
                                  default=Difficulty.EASY.value)
    treatment = models.TextField()

    # Relationships
    sicknesses = models.ManyToManyField(Sickness, related_name="plants_related", blank=True)
    characteristics = models.ManyToManyField('Characteristic', related_name="characteristic_plants", blank=True)

    def __str__(self):
        return self.name


class Opinion(models.Model):
    # Attributes
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Relationships
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " - " + self.plant.name


class Characteristic(models.Model):
    # Attributes
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
