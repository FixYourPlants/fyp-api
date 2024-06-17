import uuid
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token
import uuid

class User(AbstractUser):
    # Attributes
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to="users/", null=True, blank=True, default="users/default.png")
    about_me = models.TextField(null=True, blank=True, default='')
    email_verified = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    googleAccount = models.BooleanField(default=False)

    # Relationships
    favourite_plant = models.ManyToManyField('plants.Plant', blank=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        try:
            # If updating the user, delete the old image if a new image is set
            old_user = User.objects.get(pk=self.pk)
            if old_user.image and old_user.image != self.image:
                old_user.image.delete(save=False)
        except User.DoesNotExist:
            pass  # User is new, so no old image to delete

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the image when the user is deleted
        if self.image:
            self.image.delete(save=False)
        super().delete(*args, **kwargs)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


