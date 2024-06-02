from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from app.permissions import IsUserOrReadOnly
from app.plants.models import Plant, Opinion, Characteristic
from app.plants.serializers import PlantSerializer, OpinionSerializer, CharacteristicSerializer, PlantFavSerializer

# Create your views here.
'''
PLANT
'''

class PlantListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = PlantSerializer
    queryset = Plant.objects.all().order_by("id")
    permission_classes = (AllowAny,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="List of Plants",
        tags=['Plant']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PlantCreateView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="Create a Plant",
        tags=['Plant']
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PlantDetailView(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()
    permission_classes = (AllowAny,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="Retrieve a Plant",
        tags=['Plant']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class PlantUpdateAndDestroyView(viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="Update a Plant",
        tags=['Plant']
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a Plant",
        tags=['Plant']
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class PlantFavListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None

    def get_queryset(self):
        user = self.request.user
        return user.fav_plants.all()

    @swagger_auto_schema(
        operation_summary="List of Favorite Plants",
        tags=['Plant']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PlantFavChangeView(viewsets.GenericViewSet, APIView):
    serializer_class = PlantFavSerializer
    queryset = Plant.objects.all()
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None

    def perform_update(self, serializer):
        user = self.request.user
        id = self.kwargs['pk']
        plant = Plant.objects.get(id=id)

        if not user.favourite_plant.filter(id=plant.id).exists():
            user.favourite_plant.add(plant)
        else:
            user.favourite_plant.remove(plant)
        user.save()

        return user.favourite_plant.filter(id=plant.id).exists()

    @swagger_auto_schema(
        operation_summary="Add or Remove a Favorite Plant",
        tags=['Plant']
    )
    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        exists = self.perform_update(serializer)

        return Response(exists)


class PlantFavStatusView(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None

    def get_queryset(self):
        user = self.request.user
        print(user.username)
        return user.favourite_plant.all().filter(id=self.kwargs['pk'])

    @swagger_auto_schema(
        operation_summary="Retrieve a Favorite Plant",
        tags=['Plant']
    )
    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset.exists())


'''
OPINION
'''
class OpinionListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer
    permission_classes = (AllowAny,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="List of Opinions",
        tags=['Opinion']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class OpinionCreateView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="Create an Opinion",
        tags=['Opinion']
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class OpinionDetailView(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    serializer_class = OpinionSerializer
    queryset = Opinion.objects.all()
    permission_classes = (AllowAny,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="Retrieve an Opinion",
        tags=['Opinion']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class OpinionUpdateAndDestroyView(viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = OpinionSerializer
    queryset = Opinion.objects.all()
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="Update an Opinion",
        tags=['Opinion']
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete an Opinion",
        tags=['Opinion']
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


'''
CHARACTERISTIC
'''


class CharacteristicListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Characteristic.objects.all()
    serializer_class = CharacteristicSerializer
    permission_classes = (AllowAny,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="List of Characteristics",
        tags=['Characteristic']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class CharacteristicCreateView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Characteristic.objects.all()
    serializer_class = CharacteristicSerializer
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="Create a Characteristic",
        tags=['Characteristic']
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class CharacteristicDetailView(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    serializer_class = CharacteristicSerializer
    queryset = Characteristic.objects.all()
    permission_classes = (AllowAny,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="Retrieve a Characteristic",
        tags=['Characteristic']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class CharacteristicUpdateAndDestroyView(viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = CharacteristicSerializer
    queryset = Characteristic.objects.all()
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="Update a Characteristic",
        tags=['Characteristic']
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a Characteristic",
        tags=['Characteristic']
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


