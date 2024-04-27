import uuid
from django.db import models


# Create your models here.
class Sickness(models.Model):
    # Attributes
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    treatment = models.TextField()

    # Relationships
    plants = models.ManyToManyField('plants.Plant', related_name="sicknesses_related", blank=True)

    def __str__(self):
        return self.name
