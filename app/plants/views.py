from rest_framework import viewsets, mixins

from app.plants.models import Plant, Opinion, Characteristic
from app.plants.serializers import PlantSerializer, OpinionSerializer, CharacteristicSerializer

# Create your views here.
'''
PLANTS
'''


class PlantListCreateView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()


class PlantDetailView(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()


'''
OPINION
'''


class OpinionListView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer


class OpinionDetailView(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = OpinionSerializer
    queryset = Opinion.objects.all()


'''
CHARACTERISTIC
'''


class CharacteristicListView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Characteristic.objects.all()
    serializer_class = CharacteristicSerializer


class CharacteristicDetailView(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = CharacteristicSerializer
    queryset = Characteristic.objects.all()
