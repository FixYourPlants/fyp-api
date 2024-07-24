from datetime import timedelta

from django.urls import reverse
from django.utils import timezone
from pytz import timezone as pytz_timezone
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from app.notification.tests.factories import NotificationFactory
from app.plants.tests.factories import PlantFactory
from app.sickness.tests.factories import SicknessFactory
from app.users.tests.factories import UserFactory


class TestNotificationListView(APITestCase):

    def setUp(self):
        self.user = UserFactory()

        refresh = RefreshToken.for_user(self.user)
        access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        self.url = reverse('notification-list')

        self.plant = PlantFactory()
        self.sickness = SicknessFactory()
        self.notification1 = NotificationFactory(timestamp=timezone.now().astimezone(pytz_timezone('UTC')) - timedelta(hours=1))
        self.notification2 = NotificationFactory(timestamp=timezone.now().astimezone(pytz_timezone('UTC')) - timedelta(hours=2))

        self.user.favourite_plant.add(self.plant)
        self.user.affected_sicknesses.add(self.sickness)

        self.plant.notifications.add(self.notification1)
        self.sickness.notifications.add(self.notification2)

    def test_list_notifications_without_time_filters(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_list_notifications_with_start_time_filter(self):
        start_time = (timezone.now().astimezone(pytz_timezone('UTC')) - timedelta(hours=1, minutes=30)).strftime('%H:%M:%S')
        response = self.client.get(self.url, {'start_time': start_time})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], str(self.notification1.id))

    def test_list_notifications_with_end_time_filter(self):
        end_time = (timezone.now().astimezone(pytz_timezone('UTC')) - timedelta(hours=1, minutes=30)).strftime('%H:%M:%S')
        response = self.client.get(self.url, {'end_time': end_time})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], str(self.notification2.id))

    def test_list_notifications_with_start_and_end_time_filters(self):
        start_time = (timezone.now().astimezone(pytz_timezone('UTC')) - timedelta(hours=4, minutes=30)).strftime('%H:%M:%S')
        end_time = (timezone.now().astimezone(pytz_timezone('UTC')) + timedelta(hours=0, minutes=30)).strftime('%H:%M:%S')
        response = self.client.get(self.url, {'start_time': start_time, 'end_time': end_time})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


