from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app.users.tests.factories import UserFactory


class TestUserListView(APITestCase):
    """
    Tests /users list operations and get_user_id_by_username endpoint.
    """

    def setUp(self):
        self.user = UserFactory()
        self.user2 = UserFactory(username='testuser2')
        self.list_url = reverse('user-list-list')
        self.get_user_id_url = reverse('user-list-get-user-id-by-username')
        self.user_data = {'username': 'testuser', 'password': 'securepassword123'}

    def test_list_users(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data)

    def test_get_user_id_by_username_success(self):
        response = self.client.get(self.get_user_id_url, {'username': self.user2.username})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(str(response.data['user_id']), self.user2.id)

    def test_get_user_id_by_username_failure(self):
        response = self.client.get(self.get_user_id_url, {'username': 'nonexistent'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'User not found')

    def test_get_user_id_by_username_no_username(self):
        response = self.client.get(self.get_user_id_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Username not provided')




