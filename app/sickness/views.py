from drf_yasg import openapi
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from app.permissions import IsUserOrReadOnly
from app.sickness.models import Sickness
from app.sickness.serializers import SicknessSerializer

# Create your views here.
'''
SICKNESS
'''


from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from app.permissions import IsUserOrReadOnly
from app.sickness.models import Sickness
from app.sickness.serializers import SicknessSerializer

# Create your views here.
'''
SICKNESS
'''


class SicknessListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Sickness.objects.all()
    serializer_class = SicknessSerializer
    permission_classes = (AllowAny,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="List of Sicknesses",
        tags=['Sickness']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class SicknessCreateView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Sickness.objects.all()
    serializer_class = SicknessSerializer
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="Create a Sickness",
        tags=['Sickness']
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class SicknessDetailView(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = Sickness.objects.all()
    serializer_class = SicknessSerializer
    permission_classes = (AllowAny,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="Retrieve a Sickness",
        tags=['Sickness']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)



class PlantsWithSicknessListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = SicknessSerializer
    queryset = Sickness.objects.all().order_by("id")
    permission_classes = (AllowAny,)
    pagination_class = None


    def get_queryset(self):
        sickness_id = self.kwargs.get('sickness_id')
        return Sickness.objects.get(id=sickness_id).plants_related.all()

    @swagger_auto_schema(
        operation_summary="List of Plants with a Sickness",
        tags=['Sickness'],
        manual_parameters=[
            openapi.Parameter(
                name='sickness_id',
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                required=True,
                description='ID of the sickness to filter plants'
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
