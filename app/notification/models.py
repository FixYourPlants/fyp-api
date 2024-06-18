from django.db import models
import uuid

# Create your models here.
class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    timestamp = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.title