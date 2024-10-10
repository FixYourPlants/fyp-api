from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from unittest.mock import patch
import requests


class TestAlertListViewGov(APITestCase):
    def test_list_alerts_success(self):
        url = reverse('alert-list-gob-list')  # Asegúrate de que esta es la URL correcta
        response = self.client.get(url)

        # Verifica que el estado de la respuesta sea 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifica que la respuesta contenga los campos esperados
        for alert in response.data:
            self.assertIn('title', alert)
            self.assertIn('image', alert)
            self.assertIn('family', alert)
            self.assertIn('distribution', alert)
            self.assertIn('host', alert)
            self.assertIn('damage', alert)
