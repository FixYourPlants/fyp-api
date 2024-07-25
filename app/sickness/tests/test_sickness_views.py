from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from app.plants.tests.factories import PlantFactory
from app.sickness.tests.factories import SicknessFactory
from app.users.tests.factories import UserFactory


class TestSicknessListView(APITestCase):

    def setUp(self):
        self.url = reverse('sickness-list-list')
        SicknessFactory.create_batch(2)

    def test_list_sicknesses(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class TestPlantsWithSicknessListView(APITestCase):

    def setUp(self):
        self.sickness = SicknessFactory()
        self.plant = PlantFactory()
        self.plant.sicknesses.add(self.sickness)
        self.plant.save()
        self.url = reverse('plants-with-sickness-list-list') + f'?sickness={self.sickness.id}'

    def test_list_plants_with_sickness(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], str(self.plant.id))


class TestSicknessAffectedChangeView(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.sickness = SicknessFactory()
        refresh = RefreshToken.for_user(self.user)
        access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        self.url = reverse('sickness-affected-change-detail', args=[self.sickness.id])

    def test_add_remove_affected_sickness(self):
        # Add sickness
        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.user.affected_sicknesses.filter(id=self.sickness.id).exists())

        # Remove sickness
        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(self.user.affected_sicknesses.filter(id=self.sickness.id).exists())


class TestSicknessAffectedStatusView(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.sickness = SicknessFactory()
        self.user.affected_sicknesses.add(self.sickness)
        refresh = RefreshToken.for_user(self.user)
        access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        self.url = reverse('sickness-affected-status-detail', args=[self.sickness.id])

    def test_affected_sickness_status(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data)

