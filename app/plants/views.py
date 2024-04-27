from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from app.permissions import IsUserOrReadOnly
from app.plants.models import Plant, Opinion, Characteristic
from app.plants.serializers import PlantSerializer, OpinionSerializer, CharacteristicSerializer

# Create your views here.
'''
PLANT
'''


class PlantListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = PlantSerializer
    queryset = Plant.objects.all().order_by("id")
    permission_classes = (AllowAny,)
    pagination_class = None


class PlantCreateView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None


class PlantDetailView(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()
    permission_classes = (AllowAny,)
    pagination_class = None


class PlantUpdateAndDestroyView(viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None


class PlantFavListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None

    def get_queryset(self):
        user = self.request.user
        return user.fav_plants.all()


class PlantFavCreateView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None

    def perform_create(self, serializer):
        user = self.request.user
        plant = serializer.save()
        user.fav_plants.add(plant)


class PlantFavDestroyView(viewsets.GenericViewSet, mixins.DestroyModelMixin):
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None

    def perform_destroy(self, instance):
        user = self.request.user
        user.fav_plants.remove(instance)


'''
OPINION
'''


class OpinionListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer
    permission_classes = (AllowAny,)
    pagination_class = None


class OpinionCreateView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None


class OpinionDetailView(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    serializer_class = OpinionSerializer
    queryset = Opinion.objects.all()
    permission_classes = (AllowAny,)
    pagination_class = None


class OpinionUpdateAndDestroyView(viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = OpinionSerializer
    queryset = Opinion.objects.all()
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None


'''
CHARACTERISTIC
'''


class CharacteristicListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Characteristic.objects.all()
    serializer_class = CharacteristicSerializer
    permission_classes = (AllowAny,)
    pagination_class = None


class CharacteristicCreateView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Characteristic.objects.all()
    serializer_class = CharacteristicSerializer
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None


class CharacteristicDetailView(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    serializer_class = CharacteristicSerializer
    queryset = Characteristic.objects.all()
    permission_classes = (AllowAny,)
    pagination_class = None


class CharacteristicUpdateAndDestroyView(viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = CharacteristicSerializer
    queryset = Characteristic.objects.all()
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None

