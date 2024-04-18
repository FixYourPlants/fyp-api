from rest_framework import serializers

from app.users.serializers import UserSerializer
from .models import Diary, Page


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'

class DiarySerializer(serializers.ModelSerializer):
    pages = PageSerializer(many=True, read_only=True)
    user = UserSerializer()  # Suponiendo que tienes un serializador UserSerializer

    class Meta:
        model = Diary
        fields = '__all__'
