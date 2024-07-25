from django.forms.models import model_to_dict
from django.test import TestCase

from .factories import DiaryFactory, PageFactory
from ..serializers import DiarySerializer, DiaryCreateSerializer, PageSerializer, PageCreateSerializer
from ...plants.tests.factories import PlantFactory
from ...users.tests.factories import UserFactory


class TestDiarySerializer(TestCase):

    def setUp(self):
        self.plant = PlantFactory.create()
        self.user = UserFactory.create()
        diary = DiaryFactory.build(plant=self.plant, user=self.user)
        self.diary_data = model_to_dict(diary)
        self.diary_data['plant'] = str(diary.plant.id)
        self.diary_data['user'] = str(diary.user.id)

    def test_serializer_with_empty_data(self):
        serializer = DiarySerializer(data={})
        self.assertFalse(serializer.is_valid())

    def test_serializer_with_valid_data(self):
        serializer = DiaryCreateSerializer(data=self.diary_data)
        self.assertTrue(serializer.is_valid(), msg=serializer.errors)

    def test_serializer_saves_correctly(self):
        serializer = DiaryCreateSerializer(data=self.diary_data)
        self.assertTrue(serializer.is_valid(), msg=serializer.errors)
        diary = serializer.save()
        for field, value in self.diary_data.items():
            if field in ['plant', 'user']:
                self.assertEqual(str(getattr(diary, field).id), value)
            else:
                self.assertEqual(getattr(diary, field), value)

class TestPageSerializer(TestCase):

    def setUp(self):
        self.diary = DiaryFactory.create()
        page = PageFactory.build(diary=self.diary)
        self.page_data = model_to_dict(page)
        self.page_data['diary'] = str(page.diary.id)

    def test_serializer_with_empty_data(self):
        serializer = PageSerializer(data={})
        self.assertFalse(serializer.is_valid())

    def test_serializer_with_valid_data(self):
        serializer = PageCreateSerializer(data=self.page_data)
        self.assertTrue(serializer.is_valid(), msg=serializer.errors)

    def test_serializer_saves_correctly(self):
        serializer = PageCreateSerializer(data=self.page_data)
        self.assertTrue(serializer.is_valid(), msg=serializer.errors)
        page = serializer.save()
        for field, value in self.page_data.items():
            if field == 'diary':
                self.assertEqual(str(getattr(page, field).id), value)
            else:
                self.assertEqual(getattr(page, field), value)


