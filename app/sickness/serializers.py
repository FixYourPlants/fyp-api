from rest_framework import serializers

from .models import Sickness



class SicknessSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sickness
        fields = '__all__'
