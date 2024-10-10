from django.forms import model_to_dict
from django.test import TestCase

from app.sickness.serializers import SicknessSerializer
from app.sickness.tests.factories import SicknessFactory


class TestSicknessSerializer(TestCase):

    def setUp(self):
        self.sickness = SicknessFactory.create()
        self.sickness_data = model_to_dict(self.sickness)

    def test_serializer_with_empty_data(self):
        serializer = SicknessSerializer(data={})
        self.assertFalse(serializer.is_valid())

    def test_serializer_with_valid_data(self):
        serializer = SicknessSerializer(data=self.sickness_data)
        self.assertTrue(serializer.is_valid(), msg=serializer.errors)