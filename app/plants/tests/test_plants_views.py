from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from app.plants.tests.factories import PlantFactory, OpinionFactory
from app.users.tests.factories import UserFactory

'''
PLANT
'''
class TestPlantListView(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.url = reverse('plant-list-list')

        PlantFactory.create_batch(2)

    def test_list_plants(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class TestPlantDetailView(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.plant = PlantFactory()
        self.url = reverse('plant-detail-detail', args=[self.plant.id])

    def test_retrieve_plant(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], str(self.plant.id))


class TestPlantFavChangeView(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        refresh = RefreshToken.for_user(self.user)
        access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        self.plant = PlantFactory()
        self.url = reverse('plant-fav-change-detail', args=[self.plant.id])

    def test_fav_change_plant(self):
        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.user.favourite_plant.filter(id=self.plant.id).exists())

        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(self.user.favourite_plant.filter(id=self.plant.id).exists())


class TestPlantFavStatusView(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        refresh = RefreshToken.for_user(self.user)
        access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        self.plant = PlantFactory()
        self.url = reverse('plant-fav-status-detail', args=[self.plant.id])

        self.user.favourite_plant.add(self.plant)

    def test_fav_status_plant(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data)

'''
OPINION
'''
class TestOpinionListView(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.plant = PlantFactory()
        self.url = reverse('opinion-list-list')

        OpinionFactory.create_batch(2, plant=self.plant)

    def test_list_opinions(self):
        response = self.client.get(self.url, {'plant_id': self.plant.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_list_opinions_without_plant_id(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class TestOpinionCreateView(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        refresh = RefreshToken.for_user(self.user)
        access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        self.plant = PlantFactory()
        self.url = reverse('opinion-create-list')

        self.opinion_data = {
            'title': 'Sample opinion title',
            'description': 'Sample opinion description',
            'plant': str(self.plant.id),
            'user': str(self.user.id),
        }

    def test_create_opinion(self):
        response = self.client.post(self.url, self.opinion_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.opinion_data['title'])
        self.assertEqual(response.data['description'], self.opinion_data['description'])

    def test_create_opinion_unauthenticated(self):
        self.client.logout()
        response = self.client.post(self.url, self.opinion_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_opinion_with_invalid_plant(self):
        self.opinion_data['plant'] = '00000000-0000-0000-0000-000000000000'
        response = self.client.post(self.url, self.opinion_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('plant', response.data)

