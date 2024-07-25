import uuid
from enum import Enum

from django.db.models import CharField, TextField, UUIDField, ImageField, Model, \
    ManyToManyField, ForeignKey, CASCADE
from django.forms import DateTimeField

from app.users.models import User


class Difficulty(Enum):
    EASY = 'FÁCIL'
    MEDIUM = 'MEDIO'
    HIGH = 'ALTA'

    @classmethod
    def choices(cls):
        return [(tag.value, tag.name) for tag in cls]

    @classmethod
    def from_value(cls, value):
        for tag in cls:
            if tag.value.upper() == value.upper():
                return tag
        raise ValueError(f"Invalid difficulty level: {value}")

    def __str__(self):
        return self.value




class Plant(Model):
    # Attributes
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=100)
    scientific_name = CharField(max_length=100)
    description = TextField()
    image = ImageField(upload_to="plants/", null=True, blank=True)
    difficulty = CharField(choices=[(tag.value, tag.value) for tag in Difficulty], max_length=10, default=Difficulty.EASY.value)
    treatment = TextField()

    # Relationships
    sicknesses = ManyToManyField('sickness.Sickness', related_name="plant_sicknesses", blank=True)
    characteristics = ManyToManyField('Characteristic', related_name="plant_characteristics", blank=True)
    notifications = ManyToManyField('notification.Notification', related_name='plant_notifications', blank=True)

    def __str__(self):
        return self.name

class History(Model):
    # Attributes
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = DateTimeField(auto_now_add=True)
    image = ImageField(upload_to="history/", null=True, blank=True)

    # Relationships
    plant = ForeignKey(Plant, on_delete=CASCADE)
    sickness = ForeignKey('sickness.Sickness', on_delete=CASCADE, null=True)

    def __str__(self):
        return str(self.created_at) + " - " + self.plant.name + " - " + self.sickness.name


class Opinion(Model):
    # Attributes
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = CharField(max_length=100)
    description = TextField()
    created_at = DateTimeField(auto_now_add=True)

    # Relationships
    plant = ForeignKey(Plant, on_delete=CASCADE)
    user = ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.title + " - " + self.plant.name


class Characteristic(Model):
    # Attributes
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=100)

    def __str__(self):
        return self.name
