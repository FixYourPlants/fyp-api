from rest_framework import serializers

from app.users.serializers import UserSerializer
from .models import Diary, Page
from ..plants.serializers import PlantSerializer


class DiarySerializer(serializers.ModelSerializer):
    plant = PlantSerializer()
    user = UserSerializer()

    class Meta:
        model = Diary
        fields = '__all__'


class PageSerializer(serializers.ModelSerializer):
    diary = DiarySerializer()

    class Meta:
        model = Page
        fields = ['id', 'title', 'content', 'image', 'diary', 'created_at']

    def create(self, validated_data):
        diary_data = validated_data.pop('diary')
        diary = Diary.objects.create(**diary_data)
        return Page.objects.create(diary=diary, **validated_data)


