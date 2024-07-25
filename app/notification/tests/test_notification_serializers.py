from django.forms.models import model_to_dict
from django.test import TestCase

from .factories import NotificationFactory
from ..serializers import NotificationSerializer


class TestNotificationSerializer(TestCase):

    def setUp(self):
        self.notification_data = model_to_dict(NotificationFactory.build())

    def test_serializer_with_empty_data(self):
        serializer = NotificationSerializer(data={})
        self.assertFalse(serializer.is_valid())

    def test_serializer_with_valid_data(self):
        serializer = NotificationSerializer(data=self.notification_data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_saves_correctly(self):
        serializer = NotificationSerializer(data=self.notification_data)
        self.assertTrue(serializer.is_valid())

        notification = serializer.save()
        for field, value in self.notification_data.items():
            self.assertEqual(getattr(notification, field), value)
