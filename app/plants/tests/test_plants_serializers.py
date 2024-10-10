from django.forms.models import model_to_dict
from django.test import TestCase

from app.plants.serializers import CharacteristicSerializer, PlantSerializer, HistorySerializer, OpinionSerializer, \
    SicknessSerializer
from app.plants.tests.factories import CharacteristicFactory, PlantFactory, HistoryFactory, OpinionFactory
from app.sickness.tests.factories import SicknessFactory
from app.users.serializers import UserSerializer
from app.users.tests.factories import UserFactory


class TestCharacteristicSerializer(TestCase):

    def setUp(self):
        self.characteristic = CharacteristicFactory.create()
        self.characteristic_data = model_to_dict(self.characteristic)

    def test_serializer_with_empty_data(self):
        serializer = CharacteristicSerializer(data={})
        self.assertFalse(serializer.is_valid())

    def test_serializer_with_valid_data(self):
        serializer = CharacteristicSerializer(data=self.characteristic_data)
        self.assertTrue(serializer.is_valid(), msg=serializer.errors)

    def test_serializer_saves_correctly(self):
        serializer = CharacteristicSerializer(data=self.characteristic_data)
        self.assertTrue(serializer.is_valid(), msg=serializer.errors)

        characteristic = serializer.save()
        for field, value in self.characteristic_data.items():
            self.assertEqual(getattr(characteristic, field), value)


class TestPlantSerializer(TestCase):

    def setUp(self):
        self.sickness = SicknessFactory.create()
        self.characteristic = CharacteristicFactory.create()
        self.plant = PlantFactory.create()
        self.plant.sicknesses.add(self.sickness)
        self.plant.characteristics.add(self.characteristic)
        self.plant.save()
        self.plant_data = model_to_dict(self.plant)
        self.plant_data['sicknesses'] = SicknessSerializer(instance=[self.sickness], many=True).data
        self.plant_data['characteristics'] = CharacteristicSerializer(instance=[self.characteristic], many=True).data
        self.plant_data['image'] = None
        for i in self.plant_data['sicknesses']:
            i['image'] = None

    def test_serializer_with_empty_data(self):
        serializer = PlantSerializer(data={})
        self.assertFalse(serializer.is_valid())

    def test_serializer_with_valid_data(self):
        serializer = PlantSerializer(data=self.plant_data)
        self.assertTrue(serializer.is_valid(), msg=serializer.errors)


class TestHistorySerializer(TestCase):

    def setUp(self):
        self.plant = PlantFactory.create()
        self.sickness = SicknessFactory.create()
        self.history = HistoryFactory.create(plant=self.plant, sickness=self.sickness)
        self.history_data = model_to_dict(self.history)
        self.history_data['id'] = str(self.history.id)
        self.history_data['image'] = None
        self.history_data['plant'] = PlantSerializer(instance=self.plant).data
        self.history_data['sickness'] = SicknessSerializer(instance=self.sickness).data
        self.history_data['plant']['image'] = None
        self.history_data['sickness']['image'] = None

    def test_serializer_with_empty_data(self):
        serializer = HistorySerializer(data={})
        self.assertFalse(serializer.is_valid())

    def test_serializer_with_valid_data(self):
        serializer = HistorySerializer(data=self.history_data)
        self.assertTrue(serializer.is_valid(), msg=serializer.errors)


class TestOpinionSerializer(TestCase):

    def setUp(self):
        self.user = UserFactory.create()
        self.plant = PlantFactory.create()
        self.opinion = OpinionFactory.create(plant=self.plant, user=self.user)
        self.opinion_data = model_to_dict(self.opinion)
        self.opinion_data['id'] = str(self.opinion.id)
        self.opinion_data['plant'] = PlantSerializer(instance=self.plant).data
        self.opinion_data['user'] = UserSerializer(instance=self.user).data
        self.opinion_data['plant']['image'] = None
        self.opinion_data['user']['image'] = None

    def test_serializer_with_valid_data(self):
        serializer = OpinionSerializer(instance=self.opinion_data)
        self.assertEqual(serializer.data, self.opinion_data)
