import os

from PIL import Image
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from keras.src.saving import load_model
from rest_framework import viewsets, mixins, serializers
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from app.diary.models import Diary
from app.permissions import IsUserOrReadOnly
from app.plants.models import Plant, Opinion, Characteristic, History
from app.plants.serializers import PlantSerializer, CharacteristicSerializer, PlantFavSerializer, \
    OpinionSerializer, OpinionCreateSerializer, ImageUploadSerializer, HistorySerializer
import numpy as np
import tensorflow as tf

from app.sickness.models import Sickness

# Create your views.py here.
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
            Diary.objects.get_or_create(user=user, plant=plant, title="Diario para " + plant.name)
        else:
            user.favourite_plant.remove(plant)
            Diary.objects.filter(user=user, plant=plant).delete()
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
        tags=['Opinion'],
        manual_parameters=[
            openapi.Parameter(
                name='plant_id',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description='ID of the plant to filter opinions'
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        plant_id = request.query_params.get('plant_id')
        if plant_id:
            self.queryset = Opinion.objects.filter(plant_id=plant_id)
        return super().list(request, *args, **kwargs)


class OpinionCreateView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Opinion.objects.all()
    serializer_class = OpinionCreateSerializer
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="Create an Opinion",
        tags=['Opinion']
    )
    def perform_create(self, serializer):
        user = self.request.user
        data = self.request.data
        plant_id = data.get('plant_id')

        try:
            plant = Plant.objects.get(id=plant_id)
        except Plant.DoesNotExist:
            raise serializers.ValidationError("Plant with the given ID does not exist")

        serializer.save(user=user, plant=plant)

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


class PlantPredictView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ImageUploadSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Load the Keras model from the .keras file
        self.model = self.load_model(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models/plant_leaf_disease_detector.keras'))

    def load_model(self, model_path):
        if not os.path.exists(model_path):
            raise ValueError(f"File not found: {model_path}. Please ensure the file is an accessible .keras zip file.")
        model = load_model(model_path)
        return model

    @swagger_auto_schema(
        operation_summary="Predict Plant from Image",
        tags=['Plant'],
        request_body=ImageUploadSerializer,
        responses={200: openapi.Response('Prediction Result')}
    )
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        image = serializer.validated_data['image']

        # Convert image to a format suitable for the prediction model
        pil_image = Image.open(image)
        processed_image = self.preprocess_image(pil_image)

        # Make prediction
        prediction_result = self.predict_plant(processed_image)

        plant = Plant.objects.filter(name=prediction_result[0]).first()
        if (prediction_result[1] == "Saludable"):
            sickness = None
        else:
            sickness = Sickness.objects.filter(name=prediction_result[1]).first()

        history = History.objects.create(plant=plant, sickness=sickness, image=image)
        request.user.history.add(history)
        request.user.save()

        return Response(HistorySerializer(history).data)

    def preprocess_image(self, image):
        # Resize the image to the size the model expects
        image = image.resize((256, 256))  # Updated size to match model input size
        # Convert the image to a numpy array and normalize it
        image_array = np.array(image) / 255.0
        # Add a batch dimension (model expects batches of images)
        image_array = np.expand_dims(image_array, axis=0)
        return image_array

    def predict_plant(self, image_array, threshold=1e-4):
        # Make a prediction
        predictions = self.model.predict(image_array)

        # Set low prediction values to zero
        predictions[predictions < threshold] = 0

        # Process the predictions as needed
        predicted_class = np.argmax(predictions, axis=1)

        # Map predicted class to plant name
        predicted_plant_name = self.map_class_to_plant(predicted_class[0])

        return predicted_plant_name

    def map_class_to_plant(self, class_index):
        # Implement the mapping from class index to plant name
        class_to_plant = {
            0: ["Manzana", "Podredumbre negra"],
            1: ["Manzana", "Mancha gris"],
            2: ["Manzana", "Saludable"],
            3: ["Manzana", "Óxido"],
            4: ["Manzana", "Sarna"],
            5: ["Pimiento Morrón", "Mancha bacteriana"],
            6: ["Pimiento Morrón", "Saludable"],
            7: ["Cereza", "Saludable"],
            8: ["Cereza", "Oídio"],
            9: ["Café", "Saludable"],
            10: ["Café", "Ácaros rojos"],
            11: ["Café", "Óxido"],
            12: ["Maíz", "Tizón"],
            13: ["Maíz", "Mancha gris"],
            14: ["Maíz", "Saludable"],
            15: ["Maíz", "Óxido"],
            16: ["Algodón", "Tizón bacteriano"],
            17: ["Algodón", "Saludable"],
            18: ["Algodón", "Oídio"],
            19: ["Algodón", "Mancha foliar"],
            20: ["Uvas", "Sarampión negro"],
            21: ["Uvas", "Podredumbre negra"],
            22: ["Uvas", "Tizón"],
            23: ["Uvas", "Saludable"],
            24: ["Melocotón", "Mancha bacteriana"],
            25: ["Melocotón", "Saludable"],
            26: ["Patata", "Tizón temprano"],
            27: ["Patata", "Saludable"],
            28: ["Patata", "Tizón tardío"],
            29: ["Arroz", "Tizón bacteriano"],
            30: ["Arroz", "Brusone"],
            31: ["Arroz", "Saludable"],
            32: ["Fresa", "Saludable"],
            33: ["Fresa", "Quemadura"],
            34: ["Fresa", "Mancha foliar"],
            35: ["Caña de azúcar", "Saludable"],
            36: ["Caña de azúcar", "Virus del mosaico"],
            37: ["Caña de azúcar", "Óxido"],
            38: ["Caña de azúcar", "Virus rizado amarillo"],
            39: ["Tomate", "Mancha bacteriana"],
            40: ["Tomate", "Tizón temprano"],
            41: ["Tomate", "Saludable"],
            42: ["Tomate", "Tizón tardío"],
            43: ["Tomate", "Moho"],
            44: ["Tomate", "Virus del mosaico"],
            45: ["Tomate", "Mancha septoria"],
            46: ["Tomate", "Mancha foliar"],
            47: ["Tomate", "Ácaros rojos"],
            48: ["Tomate", "Virus rizado amarillo"],
        }
        return class_to_plant.get(class_index, ["Índice de clase desconocido"])



