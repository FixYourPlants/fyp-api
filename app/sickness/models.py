import uuid

from django.db.models import CharField, TextField, UUIDField, ImageField, Model, \
    ManyToManyField


# Create your models here.
class Sickness(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=100)
    description = TextField()
    treatment = TextField()
    image = ImageField(upload_to="sicknesses/", null=True, blank=True)

    notifications = ManyToManyField('notification.Notification', related_name='sickness_notifications', blank=True)

    def __str__(self):
        return self.name
