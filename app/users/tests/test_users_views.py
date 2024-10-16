from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from app.users.models import User
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

class TestLoginView(APITestCase):
    """
    Tests the login operations for the LoginView.
    """

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='securepassword123',
            email='testuser@example.com',
            email_verified=True  # Simulando que el email ha sido verificado
        )
        self.login_url = reverse('login')  # Asegúrate de que esta URL sea correcta

    def test_login_success(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'securepassword123'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)
        self.assertEqual(response.data['userId'], self.user.id)
        self.assertEqual(response.data['message'], 'Login successful')

    def test_login_failure_incorrect_password(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['error'], 'Usuario o contraseña incorrectos')

    def test_login_failure_user_not_verified(self):
        # Crear un usuario sin verificar el email
        unverified_user = User.objects.create_user(
            username='unverifieduser',
            password='securepassword123',
            email='unverified@example.com',
            email_verified=False  # Email no verificado
        )

        response = self.client.post(self.login_url, {
            'username': 'unverifieduser',
            'password': 'securepassword123'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['email'], 'El email no ha sido verificado')

    def test_login_failure_nonexistent_user(self):
        response = self.client.post(self.login_url, {
            'username': 'nonexistentuser',
            'password': 'securepassword123'
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['error'], 'Usuario o contraseña incorrectos')

    def test_login_no_username(self):
        response = self.client.post(self.login_url, {
            'password': 'securepassword123'
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['error'], 'Usuario o contraseña incorrectos')



