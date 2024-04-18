from rest_framework import serializers

from .models import Treatment, Sickness


class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = '__all__'

class SicknessSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sickness
        fields = '__all__'
