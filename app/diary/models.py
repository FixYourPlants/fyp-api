from django.core.paginator import Page
from django.db import models

from app.users.models import User


# Create your models here.
class Diary(models.Model):
    # Atributos
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Relaciones
    pages = models.ManyToOneRel(Page, related_name="diaries", to="diary.Page", field_name="diary_id")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Page(models.Model):
    # Atributos
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Relaciones
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)

    def __str__(self):
        return self.diary.title