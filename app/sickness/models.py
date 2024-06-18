import uuid

from django.db import models


# Create your models here.
class Sickness(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    treatment = models.TextField()
    image = models.ImageField(upload_to="sicknesses/", null=True, blank=True)

    notifications = models.ManyToManyField('notification.Notification', related_name='sickness_notifications', blank=True)

    def __str__(self):
        return self.name
