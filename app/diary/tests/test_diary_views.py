from django.forms import model_to_dict
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from app.diary.tests.factories import DiaryFactory, PageFactory
from app.users.tests.factories import UserFactory

'''
DIARY
'''
class TestDiaryListView(APITestCase):

    def setUp(self):
        self.user = UserFactory()

        refresh = RefreshToken.for_user(self.user)
        access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        self.url = reverse('diary-list-list')

        self.diary1 = DiaryFactory(user=self.user)
        self.diary2 = DiaryFactory(user=self.user)

    def test_list_diaries(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['id'], str(self.diary1.id))
        self.assertEqual(response.data[1]['id'], str(self.diary2.id))

    def test_list_diaries_unauthenticated(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

'''
PAGE
'''
class TestPageListView(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        refresh = RefreshToken.for_user(self.user)
        access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        self.diary = DiaryFactory(user=self.user)
        self.page1 = PageFactory(diary=self.diary)
        self.page2 = PageFactory(diary=self.diary)
        self.url = reverse('page-list-list')

    def test_list_pages_with_diary_id(self):
        response = self.client.get(self.url, {'diary_id': self.diary.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['id'], str(self.page1.id))
        self.assertEqual(response.data[1]['id'], str(self.page2.id))

    def test_list_pages_without_diary_id(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_list_pages_unauthenticated(self):
        self.client.logout()
        response = self.client.get(self.url, {'diary_id': self.diary.id})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class TestPageCreateView(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        refresh = RefreshToken.for_user(self.user)
        access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        self.diary = DiaryFactory(user=self.user)
        self.url = reverse('page-create-list')
        self.page = PageFactory(diary=self.diary)
        self.page_data = model_to_dict(self.page)

    def test_create_page(self):
        response = self.client.post(self.url, self.page_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.page_data['title'])
        self.assertEqual(response.data['content'], self.page_data['content'])



    def test_create_page_unauthenticated(self):
        self.client.logout()
        response = self.client.post(self.url, self.page_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_page_with_invalid_diary(self):
        self.page_data['diary'] = 'invalid_diary_id'
        response = self.client.post(self.url, self.page_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



