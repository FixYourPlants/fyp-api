import uuid

from django.db.models import CharField, TextField, UUIDField, Model
from django.forms import DateTimeField


# Create your models here.
class Notification(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = CharField(max_length=200)
    timestamp = DateTimeField()
    description = TextField()

    def __str__(self):
        return self.title