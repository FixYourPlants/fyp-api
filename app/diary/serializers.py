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
        fields = '__all__'

