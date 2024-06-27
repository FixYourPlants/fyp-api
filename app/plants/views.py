from PIL import Image
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins, serializers
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from app.diary.models import Diary
from app.permissions import IsUserOrReadOnly
from app.plants.models import Plant, Opinion, Characteristic
from app.plants.serializers import PlantSerializer, CharacteristicSerializer, PlantFavSerializer, \
    OpinionSerializer, OpinionCreateSerializer, ImageUploadSerializer
import numpy as np
import tensorflow as tf

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

'''
class PlantPredictView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ImageUploadSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Load the Keras model from the .pb file
        self.model = self.load_model('saved_model.pb')

    def load_model(self, model_path):
        model = tf.keras.models.load_model(model_path)
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

        return Response({'prediction': prediction_result})

    def preprocess_image(self, image):
        # Resize the image to the size the model expects
        image = image.resize((224, 224))  # Example size, replace with your model's input size
        # Convert the image to a numpy array and normalize it
        image_array = np.array(image) / 255.0
        # Add a batch dimension (model expects batches of images)
        image_array = np.expand_dims(image_array, axis=0)
        return image_array

    def predict_plant(self, image_array):
        # Make a prediction
        predictions = self.model.predict(image_array)
        # Process the predictions as needed
        predicted_class = np.argmax(predictions, axis=1)
        # Map predicted class to plant name
        predicted_plant_name = self.map_class_to_plant(predicted_class[0])
        return predicted_plant_name

    def map_class_to_plant(self, class_index):
        # Implement the mapping from class index to plant name
        class_to_plant = {
            0: "Rose",
            1: "Tulip",
            2: "Daisy",
        }
        return class_to_plant.get(class_index, "Unknown Plant")
        '''
