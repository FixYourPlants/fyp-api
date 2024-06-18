import uuid

from django.db import models

from app.users.models import User


# Create your models here.
class Diary(models.Model):
    # Atributos
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

    # Relaciones
    plant = models.ForeignKey('plants.Plant', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Page(models.Model):
    # Attributes
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="pages/", null=True, blank=True)

    # Relationships
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)

    def __str__(self):
        return self.diary.title