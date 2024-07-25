import uuid

from django.db.models import CharField, TextField, UUIDField, ImageField, Model, \
    ForeignKey, CASCADE
from django.forms import DateTimeField

from app.users.models import User


# Create your models here.
class Diary(Model):
    # Attributes
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = CharField(max_length=255)
    updated_at = DateTimeField(auto_now=True)

    # Relationships
    plant = ForeignKey('plants.Plant', on_delete=CASCADE)
    user = ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.title

class Page(Model):
    # Attributes
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = CharField(max_length=255)
    content = TextField()
    created_at = DateTimeField(auto_now_add=True)
    image = ImageField(upload_to="pages/", null=True, blank=True)

    # Relationships
    diary = ForeignKey(Diary, on_delete=CASCADE)

    def __str__(self):
        return self.diary.title