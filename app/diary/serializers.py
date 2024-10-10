from rest_framework import serializers

from app.users.serializers import UserSerializer
from .models import Diary, Page
from ..plants.serializers import PlantSerializer

'''
DIARY
'''
class DiarySerializer(serializers.ModelSerializer):
    plant = PlantSerializer()
    user = UserSerializer()

    class Meta:
        model = Diary
        fields = '__all__'


class DiaryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ['id', 'title', 'plant', 'user']
        extra_kwargs = {
            'plant': {'write_only': True},
            'user': {'write_only': True}
        }

'''
PAGE
'''
class PageSerializer(serializers.ModelSerializer):
    diary = DiarySerializer()

    class Meta:
        model = Page
        fields = ['id', 'title', 'content', 'image', 'diary', 'created_at']

class PageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['id', 'title', 'content', 'image', 'diary']
        extra_kwargs = {
            'diary': {'write_only': True}
        }
