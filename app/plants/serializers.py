from rest_framework import serializers

from app.plants.models import Plant, Difficulty, History, Opinion, Characteristic
from app.users.serializers import UserSerializer
from ..sickness.models import Sickness


from rest_framework import serializers
from app.plants.models import Plant, Difficulty, History, Opinion, Characteristic
from app.users.serializers import UserSerializer

from rest_framework import serializers
from app.plants.models import Difficulty

from rest_framework import serializers

from rest_framework import serializers


class SicknessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sickness
        fields = '__all__'

class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = '__all__'

class PlantSerializer(serializers.ModelSerializer):
    sicknesses = SicknessSerializer(required=False, many=True)
    characteristics = CharacteristicSerializer(required=False, many=True)

    class Meta:
        model = Plant
        fields = '__all__'

class PlantFavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['id']

class HistorySerializer(serializers.ModelSerializer):
    plant = PlantSerializer()
    sickness = SicknessSerializer()

    class Meta:
        model = History
        fields = '__all__'

class OpinionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = ['id', 'title', 'description', 'plant', 'user', 'created_at']
        read_only_fields = ['id', 'created_at']
        extra_kwargs = {
            'plant': {'write_only': True},
            'user': {'write_only': True}
        }

class OpinionSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    plant = PlantSerializer()

    class Meta:
        model = Opinion
        fields = '__all__'

class ImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField()




