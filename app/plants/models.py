from enum import Enum

from django.db import models

from app.diary.models import Diary
from app.sickness.models import Sickness, Treatment
from app.users.models import User


# Create your models here.
class Plant(models.Model):
    # Atributos
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="plants/")
    difficulty = models.IntegerField()

    # Relaciones
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE, related_name="treatment_plants")
    sicknesses = models.ManyToManyField(Sickness, related_name="sickness_plants")
    characteristics = models.ManyToManyField('Characteristic', related_name="characteristic_plants")
    diary = models.ManyToOneRel('Diary', related_name="diary_plants", to=Diary, field_name="plant_id")


    def __str__(self):
        return self.name

class Opinion(models.Model):
    # Atributos
    title = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Relaciones
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " - " + self.plant.name + " - " + self.email

class Characteristic(models.Model):
    # Atributos
    name = models.CharField(max_length=100)

    # Relaciones
    plant = models.ManyToManyField(Plant, related_name="plant_characteristics")

    def __str__(self):
        return self.name

class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3
