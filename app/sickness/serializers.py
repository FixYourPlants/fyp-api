from rest_framework import serializers

from .models import Sickness
from ..plants.serializers import PlantSerializer


class SicknessSerializer(serializers.ModelSerializer):
    plant = PlantSerializer(many=True, read_only=True)

    class Meta:
        model = Sickness
        fields = '__all__'
