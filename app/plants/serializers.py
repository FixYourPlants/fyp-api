from rest_framework import serializers

from app.diary.serializers import DiarySerializer
from app.sickness.serializers import SicknessSerializer
from app.users.serializers import UserSerializer
from .models import Plant, Opinion, Characteristic, Difficulty


class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = '__all__'

class DifficultySerializer(serializers.Serializer):
    def to_representation(self, instance):
        return instance.value

class PlantSerializer(serializers.ModelSerializer):
    sickness = SicknessSerializer(many=True)
    characteristics = CharacteristicSerializer(many=True)
    diary = DiarySerializer()

    class Meta:
        model = Plant
        fields = '__all__'

class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = '__all__'

class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = '__all__'

class DifficultyField(serializers.Field):
    def to_representation(self, obj):
        return obj

    def to_internal_value(self, data):
        try:
            return Difficulty[data.upper()]
        except KeyError:
            raise serializers.ValidationError("Invalid difficulty level")

class PlantSerializer(serializers.ModelSerializer):
    difficulty = DifficultyField()
    sicknesses = SicknessSerializer(many=True)
    characteristics = CharacteristicSerializer(many=True)

    class Meta:
        model = Plant
        fields = '__all__'
